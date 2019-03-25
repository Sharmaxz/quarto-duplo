from django.db import models
from django.contrib import admin


class User(models.Model):
    """
        Setting my User field where cpf and email are unique. And all
        fields need to be fill.
    """
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=False, null=False)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=200, unique=True)

    """"
        What's the Meta?
        
        This is just a class container with some options (metadata) 
        attached to the model. It defines such things as available 
        permissions, associated database table name, whether the model 
        is abstract or not, singular and plural versions of the name etc.
    """

    class Meta:
        abstract = False
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"

    """
        What's the __str__?
        
        Use __str__ if you have a class, and you'll want an informative/informal 
        output, whenever you use this object as part of string. E.g. you can 
        define __str__ methods for Django models, which then gets rendered in 
        the Django administration interface. Instead of something like 
        <Model object> you'll get like first and last name of a person, the name 
        and date of an event, etc.
    """

    def __str__(self):
        return self.name

    """
        About @classmethod and @staticmethod
        https://www.programiz.com/python-programming/methods/built-in/classmethod
    """

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'cpf', 'email')

