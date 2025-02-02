from django.contrib import admin
from . import models


class ResumeGalleryadmin(admin.TabularInline):
    model = models.ResumeGallery
    extra = 1


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [ResumeGalleryadmin]


admin.site.register(models.ResumeCategory)
