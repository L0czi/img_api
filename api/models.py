from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

class Account(models.Model):
    USER_TIER = (
        ("BASIC", "Basic"),
        ("PREMIUM", "Premium")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.CharField(choices=USER_TIER, default="BASIC", max_length=32)

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
