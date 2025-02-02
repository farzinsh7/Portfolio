from django.contrib import admin
from . import models


class Servicesadmin(admin.TabularInline):
    model = models.Services
    extra = 1


@admin.register(models.ServicesSummary)
class ServicesSummaryAdmin(admin.ModelAdmin):
    inlines = [Servicesadmin]
