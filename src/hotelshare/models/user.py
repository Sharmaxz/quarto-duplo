from django.db import models
from django.contrib import admin


class User(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=False)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=200)

    class Meta:
        abstract = False
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"

    def __str__(self):
        return self.name

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'cpf', 'email')
