from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from tricyhelp.models import *

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True, 'class':'form-control', 'placeholder':'Current Password'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'New Password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Confirm Password'}))

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))

class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class ComplaintInformationForm(forms.ModelForm):
    class Meta:
        model = ComplaintInformation
        fields = ['cname','address','phone_number']
        widgets = {
            'cname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juana Dela Cruz'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'MCLL Highway, Zamboanga City'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'09754894517'}),
        }

class TricycleInformationForm(forms.ModelForm):
    class Meta:
        model = ComplaintInformation
        fields = ['dname','zone','d_address','plate_number','operator_number']
        widgets = {
            'dname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juan Dela Cruz'}),
            'zone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'ZONE III 123456'}),
            'd_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'MCLL Highway, Zamboanga City'}),
            'plate_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Plate Number'}),
            'operator_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'09754894517'}),
        }

class IncidentInformationForm(forms.ModelForm):
    class Meta:
        model = ComplaintInformation
        fields = ['accident_date','accident_time','accident_place','violation_type','complaint_description','complaint_evidence']
        widgets = {
            'accident_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'accident_time':forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'accident_place':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Accident Place'}),
            'violation_type':forms.Select(attrs={'class':'form-control', 'placeholder':'Ex. Cabatangan'}),
            'complaint_description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description about the incident'}),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juan Dela Cruz'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'juandelacruz@gmail.com'}),
            'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the message'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body of the message'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cname','address','phone_number','profile_picture']
        widgets = {
            'cname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juan Dela Cruz'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'MCLL Highway Putik Zamboanga City'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
        }
