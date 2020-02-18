from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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
            return self.first_name + " " + self.last_name        
    
    @property
    def getFullAddress(self):
        if (self.address_2 is not None and self.address_2 != ""):
            return self.address_1 + " " + self.address_2 + " " + self.city + ", " + self.state + " " + self.zip
        else:
            return self.address_1 + " " + self.city + ", " + self.state + " " + self.zip

    def __str__(self):
        return self.getFullName    