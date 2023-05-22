from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input_email'}),
        error_messages={'invalid': 'Please enter a valid email address'}
    )

    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_email'}),
        error_messages={
            'invalid': '<p class="error-message">Пожалуйста введите действительное имя пользователя</p>',
            'unique': '<p class="error-message">Данный username уже есть в системе</p>',
        }
    )

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_email'})
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_email'})
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input_email', 'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'input_email', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    error_messages = {
        'password_mismatch': '<p class="error-message">Пароли не совпадают</p>',
    }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2