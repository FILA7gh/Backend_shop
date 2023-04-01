from django.db import models
from django.contrib.auth.models import User


# class ConfirmationCode(models.Model):
#     code = models.CharField(max_length=6)


class NewUser(User):
    code = models.CharField(max_length=6)
    # code = models.OneToOneField(ConfirmationCode, on_delete=models.CASCADE)
