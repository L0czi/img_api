from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Tier(models.Model):
    tier_name = models.CharField(max_length=30)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.tier_name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Account"
    
    class Meta:
        ordering = ["id"]


class Image(models.Model):
    owner = models.ForeignKey(
        Account, related_name="images", on_delete=models.CASCADE)
    image = ImageField(upload_to="images")

    class Meta:
        ordering = ["id"]
