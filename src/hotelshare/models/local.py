from django.contrib import admin
from django.db import models


class Local(models.Model):
    adress = models.CharField(max_length=300, default='')
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        abstract = False
        verbose_name_plural = "Locais"
        verbose_name = "Local"

    def __str__(self):
        return '{} {} {}'.format(self.adress, self.city, self.state)

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('adress', 'city', 'state', 'country')
