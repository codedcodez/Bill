from django.db import models

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
