from django.contrib import admin
from django.db import models


class Local(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    request = models.ForeignKey('Request', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = False
        verbose_name_plural = "Locais"
        verbose_name = "Local"
    def __str__(self):
        return '{} {} {}'.format(self.country, self.state, self.city)

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('country', 'state', 'city', 'request', 'hotel', 'event')
