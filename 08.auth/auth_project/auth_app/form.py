from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

  class Meta:
    model = User
    fields = ['username', 'password', 'password_confirm']
    help_texts = {
      'username': '必填。150字以內。可包含英文、數字與 @/./+/-/_ 符號。',
    }
  
  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    password_confirm = cleaned_data.get('password_confirm')
    if password and password_confirm and password != password_confirm:
      raise forms.ValidationError("Passwords do not match")
    return cleaned_data
