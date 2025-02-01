from django.contrib import admin
from . import models

# Register your models here.


class SocialMediasdmin(admin.TabularInline):
    model = models.SocialMedias
    extra = 1
    max_num = 5


@admin.register(models.Website)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [SocialMediasdmin]


admin.site.register(models.MyInformation)
admin.site.register(models.Skills)
