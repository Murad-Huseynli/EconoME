from django.urls import path, include
from django.contrib.auth import views as authViews
from .views import  activate,  NewLoginView, \
    register, logoutView, user_settings, NewPasswordResetView, user_profile


urlpatterns = [

    path('activate/<str:uidb64>/<str:token>', activate, name='activate'),
    path('reset', NewPasswordResetView.as_view(),
         name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>',
         authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete',
         authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_reset/done',
         authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('login',
         NewLoginView.as_view(), name='login-view'),
    path('register', register , name='register-view'),
    path('logout', logoutView, name='logout-view'),
    path('settings', user_settings, name='user-settings'),
    path('<str:username>', user_profile, name='user-profiles')
]
