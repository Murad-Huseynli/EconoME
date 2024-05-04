from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .widgets import DatePickerInput
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext_lazy as _

class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label=_("Name"))
    last_name = forms.CharField(required=True, label=_("Surname"))
    username = forms.CharField(required=True, label=_("Username"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Confirm password"))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), label="Captcha")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'captcha']


class ProfileRegistration(forms.ModelForm):
    SEXES = (
        (1, 'Kişi'),
        (2, 'Qadın'),
    )
    mobile_number = forms.CharField(label='Mobil nömrəniz', required=True)
    birthday_date = forms.DateField(label='Doğum tarixi', widget=DatePickerInput)
    sex = forms.ChoiceField(choices=SEXES, required=True, label='Cins')

    class Meta:
        model = Profile
        fields = ['mobile_number', 'birthday_date', 'sex']
        widgets = {
            'birthday_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Doğum tarixi seçin',
                       'type': 'date'
                       }),
        }


class UserOurRegistration1(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Image of  your profile"

    class Meta:
        model = Profile
        fields = ['img']
