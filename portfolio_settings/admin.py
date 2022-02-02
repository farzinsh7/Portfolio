from django.contrib import admin
from .models import SiteSetting


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'mobile']

    class Meta:
        model = SiteSetting


admin.site.register(SiteSetting,SettingsAdmin)
