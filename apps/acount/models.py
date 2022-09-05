from enum import Enum
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models


class Role(Enum):
    USER = 'user'
    ADMIN = 'admin'
    SUBSCRIPTION = 'subscription'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', Role.USER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', Role.ADMIN)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be superuser')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    ROLE = [
        (Role.USER, Role.USER),
        (Role.ADMIN, Role.ADMIN),
        (Role.SUBSCRIPTION, Role.SUBSCRIPTION),
    ]

    email = models.EmailField(
        db_index=True,
        validators=[validators.validate_email],
        unique=True,
        blank=False,
        null=False,
        verbose_name='email'
    )

    avatar = models.ImageField(
        upload_to='photos/%y/%m/%d',
        null=True,
        blank=True,
        verbose_name='изображение'
    )

    first_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='имя'
    )

    last_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='фамилия'
    )

    role = models.CharField(
        choices=ROLE,
        default="user",
        max_length=100,
        null=False,
        blank=False,
        verbose_name="роль"
    )

    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')
    is_staff = models.BooleanField(default=False, verbose_name='персонал')
    is_active = models.BooleanField(default=True, verbose_name='активный')
    is_superuser = models.BooleanField(default=False, verbose_name='админ')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    object = UserManager()

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

