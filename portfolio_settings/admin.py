from django.contrib import admin
from .models import SiteSetting, MySkills, Services, SocialMedias


class SocialMediasdmin(admin.TabularInline):
    model = SocialMedias
    extra = 1
    max_num = 10

@admin.register(SiteSetting)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [SocialMediasdmin]
    list_display = ['__str__', 'email', 'mobile']

admin.site.register(MySkills)
admin.site.register(Services)
