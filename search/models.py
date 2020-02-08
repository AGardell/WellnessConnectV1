from django.db import models


# Create your models here.
class WellnessProfessionals(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    credentials = models.TextField(default="", null=True, blank=True)
    specialties = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        db_table = '"wellness_prof"'

    def getFullName(self):
        if (self.title is not None and self.title != ""):
            return self.title + " " + self.first_name + " " + self.last_name
        else:
            return self.first_name + " " + self.last_name        

    def __str__(self):
        return self.getFullName()
