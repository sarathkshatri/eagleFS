from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    email  = models.EmailField(max_length=25)

    def __str__(self):
        return str(self.first_name)


