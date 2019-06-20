from django.urls import include, path
from django.contrib.auth import views as auth_views
from apps.authentication.views.views import *
from apps.authentication.accounts.forms import (
    CabbageLoginForm,
    CabbagePasswordChangeForm,
    CabbagePasswordResetForm,
    CabbageSetPasswordForm
)

urlpatterns = [

    # LOGIN & LOGOUT URLS
    path('login/check/',
         cabbage_login_check,
         name='cabbage_login_check'),
    path('login/',
         auth_views.LoginView.as_view(form_class=CabbageLoginForm,
                                      template_name='authentication/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='authentication/logged_out.html'),
         name='logout'),


    # PASSWORD CHANGE URLS
    path('password_change/',
         auth_views.PasswordChangeView.as_view(form_class=CabbagePasswordChangeForm,
                                               template_name='authentication/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='authentication/password_change_done.html'),
         name='password_change_done'),


    # PASSWORD RESET URLS
    path('password_reset/',
         auth_views.PasswordResetView.as_view(form_class=CabbagePasswordResetForm,
                                              subject_template_name='authentication/password_reset_subject.txt',
                                              template_name='authentication/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='authentication/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(form_class=CabbageSetPasswordForm,
                                                     template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),
]
