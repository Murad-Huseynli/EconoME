import logging

logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect


def main(request):
    
    data = {
            'title': 'Home | Econome',
            'section_class': 'index'
    }

    if request.user.is_authenticated and request.user.is_approved is False:
        user = request.user
        if request.FILES:
            user.setApprovalDocument(request.FILES['document'])
            user.setImg(request.FILES['profile_image'])
            return redirect('main-home')

        template_name = "main/confirmation.html"
        data['user_name'] = request.user.get_full_name()
        data['user_document'] = request.user.approval_document
    elif request.user.is_authenticated and request.user.is_approved is True:
        template_name = "main/index.html"
    elif request.user.is_anonymous:
        template_name = "main/index.html"

    return render(request, template_name, data)

def about_us(request):
    template_name = "main/about_us.html"
    data = {

    }
    return render(request, template_name, data)


def in_development(request):
    template_name = "main/in_development.html"
    data = {

    }
    return render(request, template_name, data)
