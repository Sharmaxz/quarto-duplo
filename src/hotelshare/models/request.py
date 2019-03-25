from django.contrib import admin
from django.db import models

GENDER_CHOICES = (
    ('M', "Masculino" ),
    ('F', "Feminino")
)


class Request(models.Model):
    user = models.ForeignKey('user', blank=False, on_delete=models.CASCADE)
    adress = models.ForeignKey('local', blank=False, null=False, default='', on_delete=models.CASCADE)
    event = models.ForeignKey('event', blank=True, null=True, default='', on_delete=models.CASCADE)
    gender_pref = models.CharField(choices=GENDER_CHOICES, max_length=100)
    checkin = models.DateField(blank=False, null=False)
    checkout = models.DateField(blank=False, null=False)

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
    list_display = ('user', 'adress', 'gender_pref',  'checkin', 'checkout',)
