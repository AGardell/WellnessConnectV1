from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class WellnessProfessional(models.Model):
    profession = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='prof/profile_pic/', null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        db_table = '"wellness_prof"'

    @property
    def getFullName(self):
        if (self.title is not None and self.title != ""):
            return self.title + " " + self.first_name + " " + self.last_name
        else:
            return self.first_name + " " + self.last_name        
    
    @property
    def getFullAddress(self):
        if (self.address_2 is not None and self.address_2 != ""):
            return self.address_1 + " " + self.address_2 + " " + self.city + ", " + self.state + " " + self.zip
        else:
            return self.address_1 + " " + self.city + ", " + self.state + " " + self.zip


    def __str__(self):
        return self.getFullName

class EducationCredential(models.Model):
    wellness_professional = models.ForeignKey(WellnessProfessional, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=255)
    year_graduated = models.CharField(max_length=4)

    class Meta:
        db_table = '"education_credential"'    

class Specialty(models.Model):
    wellness_professional = models.ForeignKey(WellnessProfessional, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)

    class Meta:
        db_table = '"specialty"'  

class License(models.Model):
    wellness_professional = models.ForeignKey(WellnessProfessional, on_delete=models.CASCADE)          
    license_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    year = models.CharField(max_length=4)

    class Meta:
        db_table = '"license"'      

# class HoursOperation(models.Model):
#     weekdays = [
#         (1, "Sunday"),
#         (2, "Monday"),
#         (3, "Tuesday"),
#         (4, "Wednesday"),
#         (5, "Thursday"),
#         (6, "Friday"),
#         (7, "Saturday"),
#     ]

#     wellness_professional = models.ForeignKey(WellnessProfessional, on_delete=models.CASCADE)
#     day_of_week = models.IntegerField(choices=weekdays)
#     open_time = models.TimeField()
#     close_time = models.TimeField()

#     class Meta:
#         db_table = '"hours_of_operation"' 
#         ordering = ["day_of_week"]      