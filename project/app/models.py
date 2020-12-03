# Django
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# First-Party
import reversion
from address.models import AddressField
from hashid_field import HashidAutoField
from model_utils import Choices
from nameparser import HumanName
from phonenumber_field.modelfields import PhoneNumberField

# Local
from .managers import UserManager


class Person(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        default='',
    )
    formal_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Formal Name"
    )
    familiar_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Familiar Name"
    )
    greeting_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Greeting Name"
    )
    prefix = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Name Prefix',
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Last Name",
    )
    middle_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Middle Name",
    )
    nick_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Nick Name",
    )
    suffix = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Name Suffix",
    )
    address = AddressField(
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        instance = self._parse(name=self.name)
        d = instance.as_dict()
        setattr(self, 'formal_name', f'{d["title"]} {d["first"]} {d["last"]} {d["suffix"]}'.strip())
        greeting = d['nickname'] if d['nickname'] else d['first']
        setattr(self, 'greeting_name', greeting)
        setattr(self, 'familiar_name', f'{greeting} {d["last"]}'.strip())
        # Remap
        remapping = {
            'title': 'prefix',
            'first': 'first_name',
            'middle': 'middle_name',
            'last': 'last_name',
            'nickname': 'nick_name',
            'suffix': 'suffix',
        }
        for attr, val in d.items():
            setattr(self, remapping[attr], val)
        super().save(*args, **kwargs)

    @classmethod
    def _parse(cls, name):
        """
        Parses and returns a `HumanName` instance.
        """
        instance = HumanName(
            full_name=name,
        )
        return instance

    class Meta:
        abstract = True


class Brother(Person):
    id = HashidAutoField(
        primary_key=True,
    )


class User(AbstractBaseUser):
    id = HashidAutoField(
        primary_key=True,
    )
    username = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
    ]

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
