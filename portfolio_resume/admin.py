from django.contrib import admin
from portfolio_resume.models import Resume, ResumeCategory, ResumeGallery


class ResumeGalleryAdmin(admin.TabularInline):
    model = ResumeGallery
    extra = 1
    max_num = 10

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [ResumeGalleryAdmin]


admin.site.register(ResumeCategory)