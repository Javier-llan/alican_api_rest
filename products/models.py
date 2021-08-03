from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

class Product():
    name = models.CharField(max_length = 255, unique = True)
    state = models.BooleanField(default = False)
