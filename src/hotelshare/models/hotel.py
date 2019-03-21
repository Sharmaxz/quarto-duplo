from django.contrib import admin
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    adress = models.ForeignKey('local', blank=True, default='', on_delete=models.CASCADE)
    daily_min = models.DecimalField(max_digits=10, decimal_places=2)
    daily_max = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = False
        verbose_name_plural = "Hoteis"
        verbose_name = "Hotél"

    def __str__(self):
        return self.name

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name', 'adress', 'daily_min', 'daily_max')

