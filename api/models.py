from django.contrib.admin.decorators import display
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField


class Size(models.Model):
    pic_size = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.pic_size}'

class Tier(models.Model):
    tier_name = models.CharField(max_length=30)
    size = models.ManyToManyField(Size)
    generate_orginal_link = models.BooleanField()
    generate_expire_link = models.BooleanField()

    class Meta:
        ordering = ['id']

    def display_sizes(self):
        sizes = [str(s.pic_size) for s in self.size.all()]
        return ', '.join(sizes)
    display_sizes.short_description = 'Sizes'

    def __str__(self):
        return self.tier_name

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Account'

class Image(models.Model):
    owner = models.ForeignKey(Account, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')


    
    


