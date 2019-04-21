from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.
#

class User(AbstractUser):
    username = models.CharField(max_length=30,
                                blank=True,
                                null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE,
                                related_name='profile')
    dob = models.DateField(null=True,
                           blank=True)
    bio = models.TextField(max_length = 1000,
                           null=True,
                           blank=True, )

