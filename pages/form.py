from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import UploadFile


class RegisterUserForm(UserCreationForm):
  class Meta:
    model =get_user_model()
    fields=['firstName','lastName','email','password1','password2']
class uploadfile(forms.ModelForm):
 class Meta:
  model = UploadFile
  fields=['file','name']
  widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'File Name'}),

        }