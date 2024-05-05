import logging
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .forms import UserOurRegistration #, ProfileImage, ProfileRegistration
from django.shortcuts import get_object_or_404
import random
import string
from django.contrib.auth.models import  Group
from .models import User, RegularUser
from .tasks import send_email
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.files.storage import default_storage

from PIL import Image

logger = logging.getLogger(__name__)


from django.contrib.auth import login
from django.contrib.auth.views import LoginView

class NewLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


    def get_context_data(self, **kwards):
        ctx = super(NewLoginView, self).get_context_data(**kwards)
        ctx['title'] = 'Login | Econome'
        ctx['section_class'] = 'sign_in_out'
        return ctx

    def form_valid(self, form):
        # Perform login process
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Use Django's built-in login function to authenticate the user
        user = form.get_user()
        login(self.request, user)

        # Redirect the user to a specific page after successful login
        next_page = self.request.POST['next']
        if len(next_page) == 0:
            next_page = '/' + self.request.LANGUAGE_CODE
       

        messages.success(self.request, 'You have successfully logged in. Lets get started!')
        response = HttpResponseRedirect(next_page)

        return response


    def form_invalid(self, form):
        errors = []
        all_errors = form.errors.get('__all__')
        if all_errors:
            errors.append(('__all__', None, all_errors))

        for field_name, error_list in form.errors.items():
            if field_name != '__all__':
                field_label = form.fields[field_name].label
                field_errors = error_list
                errors.append((field_name, field_label, field_errors))

        context = self.get_context_data(form=form)
        context['errors'] = errors
        return self.render_to_response(context)


from django.contrib.auth.views import PasswordResetView


class NewPasswordResetView(PasswordResetView):
    template_name = 'users/pass_reset.html'
    email_template_name = 'users/password_reset_email.html'
    from_email = os.getenv('mail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom variables to the context
        context['section_class'] = 'sign_in_out'
        return context

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }

        users = list(form.get_users(form.cleaned_data["email"]))

        if len(users) == 0:
            messages.error(self.request, 'There is no such account, or your account is not activated!')
            return redirect('pass-reset')

        form.save(**opts)

        return super().form_valid(form)


@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('main-home')

    if request.method == "POST":
        form = UserOurRegistration(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            username = form.cleaned_data.get('username')

            
            messages.success(request, 'Dear user ' + username + ' Thank you for joining our platform! ' + 
                             'Our administrator will send you mail when your account will be activated!')
            
            return redirect('login-view')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html',
                  {'form': form, 'title': 'Registration', 'section_class': 'sign_in_out'})


def logoutView(request):
    messages.success(request, _('You have been logged out.'))
    logout(request)
    request.session.clear()
    response = redirect('main-home')
    return response


# User settings
@login_required(login_url='login-view')
def user_settings(request):
    user = request.user
    profile = request.user.profile
    if request.POST and 'change-picture' in request.POST:
        if 'profile-image' in request.FILES:
            image = request.FILES['profile-image']
            profile.img = image
            profile.save()

            img = Image.open(profile.img.path)
    

            if img.height > 256 or img.width > 256:
                resize = (256, 256)
                img.thumbnail(resize)
                img.save(profile.img.path)
               
        else:
            profile.img = 'default.svg'
            profile.save()
        messages.success(request, "Changes were saved successfully!")

    if request.POST and 'change-info' in request.POST:
        bio = request.POST['bio']
        workplace = request.POST['workplace']
        education = request.POST['education']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile.bio = bio
        sig = 0
        if len(workplace) >= 80:
            sig = 1
            messages.error(request, _("Length of workplace must be less 80 characters!"))
        else:
            profile.workplace = workplace

        if len(education) >= 80:
            sig = 1
            messages.error(request, _("Length of education must be less 80 characters!"))
        else:
            profile.education = education

        profile.save()

        if sig == 0:
            messages.success(request, _("Changes were saved successfully!"))

    template_name = 'users/user_settings.html'
    data = {
        'section_class': 'settings',
        'user': user,
        'title': 'CodeAny | Settings'
    }

    return render(request, template_name, data)


# User profile
def user_profile(request, username):
    template_name = 'users/profile/user_profile.html'
    user = get_object_or_404(User, username=username)
    profile = user.profile
    if request.POST:
        pass

    
    data = {
        'title': 'CodeAny | Profile',
        'section_class': 'profile',
        'profile': profile.get_profile()
    }

    return render(request, template_name, data)
