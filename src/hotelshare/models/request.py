from django.contrib import admin
from django.db import models
from . import user

GENDER_CHOICES = (
    ('M', "Masculino" ),
    ('F', "Feminino")
)


class Request(models.Model):
    checkin = models.DateField(blank=False, null=False)
    checkout = models.DateField(blank=False, null=False)
    gender_pref = models.CharField(choices=GENDER_CHOICES, max_length=100)
    user = models.ForeignKey(user.User, blank=False, on_delete=models.CASCADE)

    class Meta:
        abstract = False
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"

    def __str__(self):
        return self.user.name

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'gender_pref', 'user')
