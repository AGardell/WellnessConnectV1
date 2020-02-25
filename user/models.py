from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        db_table = '"user"'

    @property
    def getFullName(self):
            return self.user.first_name + " " + self.user.last_name        
    
    @property
    def getFullAddress(self):
        if (self.address_2 is not None and self.address_2 != ""):
            return self.address_1 + " " + self.address_2 + " " + self.city + ", " + self.state + " " + self.zip
        else:
            return self.address_1 + " " + self.city + ", " + self.state + " " + self.zip

    def __str__(self):
        return self.getFullName    

    @receiver(post_save, sender=User)
    def create_member_profile(sender, instance, created, **kwargs):
        if created:
            Member.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_member_profile(sender, instance, **kwargs):
        instance.member.save()