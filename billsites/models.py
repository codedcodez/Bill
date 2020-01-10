from django.db import models
from django.contrib.auth.models import User

class SoftwareTwoFifty(models.Model):
    name = models.CharField(max_length=100)
    software = models.FileField(upload_to="executable/", max_length=100)

    def __str__(self):
        return self.name


class SoftwareFiveHundred(models.Model):
    name = models.CharField(max_length=100)
    software = models.FileField(upload_to="executable/", max_length=100)

    def __str__(self):
        return self.name


class SoftwareSevenFifty(models.Model):
    name = models.CharField(max_length=100)
    software = models.FileField(upload_to="executable/", max_length=100)

    def __str__(self):
        return self.name


class AddressUpload(models.Model):
    wallet = models.CharField(max_length=250)

    def __str__(self):
        return self.wallet


class MobileWebSoftware(models.Model):
    username = models.CharField(max_length=250)
    wallet = models.CharField(max_length=250, verbose_name='Bitcoin Wallet')
    country = models.CharField(max_length=250)
    key = models.CharField(max_length=30, verbose_name='Licence Key')
    # user_check = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
