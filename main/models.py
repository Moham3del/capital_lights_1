


from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ar_full_name = models.CharField(max_length=50, null=True, blank=True)
    en_full_name = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="profile"
        ordering = ['user']

@receiver(post_save, sender=User)
def creat_level(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(user=instance)


class User_Permission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_Permission"


@receiver(post_save, sender=User)
def creat_ContractPermission(sender, instance, created, **kwargs):
    if created:
        User_Permission.objects.create(user=instance)


