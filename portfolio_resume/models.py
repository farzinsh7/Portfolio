import os
from django.db import models


class ResumeManager(models.Manager):
    def get_resume_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, resume_id):
        qs = self.get_queryset().filter(id=resume_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class ResumeCategory(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=150, default='title')
    description = models.TextField(max_length=300, default='description')
    client = models.CharField(max_length=150, default='user')
    website = models.CharField(max_length=150, null=True)
    Date = models.DateField(null=True)
    image = models.ImageField(upload_to="resume", null=True, blank=True)
    categories = models.ManyToManyField(ResumeCategory, blank=True)

    objects = ResumeManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/resume/{self.id}/{self.title.replace(' ', '-')}"


class ResumeGallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="resume/gallery")
    project = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, related_name='galleries')

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    from_date = models.DateField(null=True, blank=True)
    till_date = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=255)
    description = models.TextField(max_length=300, default='description')
    exprience = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, related_name='exprience')

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=255)
    from_date = models.DateField(null=True, blank=True)
    till_date = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=255)
    description = models.TextField(max_length=300, default='description')
    education = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, related_name='education')

    def __str__(self):
        return self.title
