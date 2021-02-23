from django import forms
from django.contrib.auth import get_user_model

from apps.account.utils import send_activation_mail

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'password', 'password_confirmation']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже есть')
        return email


    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Пароли не совпадают')

        return data


    def save(self, commit=True):
        user = User.objects.create(**self.cleaned_data)
        # письмо с активацией
        send_activation_mail(user)
        return user
