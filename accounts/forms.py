from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'password1', 'password2',)
        widgets = {'username': forms.TextInput(attrs={'class': 'username',
                                                      'placeholder': 'Username'}),
                   'email': forms.TextInput(attrs={'class': 'email',
                                                   'placeholder': 'Email'}),
                   'password1': forms.PasswordInput(attrs={'class': 'password',
                                                          'placeholder': 'Password'}),
                   }