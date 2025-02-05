from django.contrib import admin
from . import models

# Register your models here.


class SocialMediasadmin(admin.TabularInline):
    model = models.SocialMedias
    extra = 1
    max_num = 5


@admin.register(models.Website)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [SocialMediasadmin]


class Counteradmin(admin.TabularInline):
    model = models.Counter
    extra = 4
    max_num = 4


class Interestedadmin(admin.TabularInline):
    model = models.InterestedIn
    extra = 1


@admin.register(models.MyInformation)
class MyInformationAdmin(admin.ModelAdmin):
    inlines = [Counteradmin, Interestedadmin]


admin.site.register(models.Skills)
admin.site.register(models.ContactUs)
