# from django import forms
from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'birthday', 'email', 'phone', 'is_active', 'is_staff', 'is_superuser','profile']
        widgets = {
            'profile': forms.FileInput(attrs={'accept': 'image/*', 'class': 'hide'})
        }