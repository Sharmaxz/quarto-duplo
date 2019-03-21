from django.forms import ModelForm
from hotelshare.models import Request, User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'birthday', 'cpf', 'email']


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['checkin', 'checkout', 'gender_pref', 'user']


