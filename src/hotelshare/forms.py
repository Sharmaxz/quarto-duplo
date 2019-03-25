#from django.forms import ModelForm, widgets
from django import forms
from hotelshare.models import Request, User


class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdc-text-field__input'}))
    birthday = forms.DateField(widget=forms.SelectDateWidget())
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdc-text-field__input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdc-text-field__input'}))

    class Meta:
        model = User
        fields = ['name', 'birthday', 'cpf', 'email']


class RequestForm(forms.ModelForm):
    checkin = forms.DateField(widget=forms.SelectDateWidget())
    checkout = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Request
        fields = ['user', 'adress', 'checkin', 'checkout', 'gender_pref']


