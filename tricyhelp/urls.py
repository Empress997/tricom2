from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from tricyhelp.forms import LoginForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

app_name = 'tricyhelp'

urlpatterns = [
    path('', views.ComplaintView.as_view(), name="home"),
    path('contact-us/',views.ContactView.as_view(), name="contact"),
    
    #accounts
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/edit-profile/', views.ProfileView.as_view(), name="edit-profile"),
    path('accounts/my-complaints/',views.complaints, name="complaints"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='tricyhelp:login'), name="logout"),

    path('accounts/password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html', form_class=PasswordChangeForm, success_url='/accounts/password-change-done/'), name="password-change"),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name="password-change-done") ,

    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', form_class=PasswordResetForm, success_url='/accounts/password-reset/done/'), name="password-reset"), # Passing Success URL to Override default URL, also created password_reset_email.html due to error from our app_name in URL
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', form_class=SetPasswordForm, success_url='/accounts/password-reset-complete/'), name="password_reset_confirm"), # Passing Success URL to Override default URL
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),    
]
