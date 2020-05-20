from django.contrib import admin

# Register your models here.
from .models import WellnessProfessional, EducationCredential, License, Specialty

class EducationCredentialInline(admin.TabularInline):
    model = EducationCredential

class LicenseInline(admin.TabularInline):
    model = License

class SpecialtyInline(admin.TabularInline):
    model = Specialty

class WellnessProfessionalAdmin(admin.ModelAdmin):
    inlines = [
        EducationCredentialInline,
        LicenseInline,
        SpecialtyInline
    ]

admin.site.register(WellnessProfessional, WellnessProfessionalAdmin)
admin.site.register(EducationCredential)
admin.site.register(License)
admin.site.register(Specialty)