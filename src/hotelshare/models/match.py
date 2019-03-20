from django.contrib import admin
from django.db import models
from . import request


class Match(models.Model):
    request1 = models.ForeignKey(request.Request, related_name='request', blank=True, on_delete=models.CASCADE)
    request2 = models.ForeignKey(request.Request, related_name='request1', blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = False
        verbose_name_plural = "Combinações"
        verbose_name = "Combinação"

    def __str__(self):
        return '{} {}'.format(self.request1, self.request2)

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('request1', 'request2')
