from django.contrib import admin
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    adress = models.ForeignKey('Local', blank=True, default='', on_delete=models.CASCADE)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    site = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = False
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name', 'adress', 'start_date', 'end_date', 'site')
