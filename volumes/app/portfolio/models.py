from django.db import models


class ResumeCategory(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=150, default='title')
    description = models.TextField(default='description')
    client = models.CharField(max_length=150, default='user')
    website = models.CharField(max_length=150, null=True)
    project_date = models.DateField(null=True)
    thumbnail = models.ImageField(upload_to="resume/thumbnail")
    categories = models.ManyToManyField(ResumeCategory)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ResumeGallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="resume/gallery")
    gallery = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, related_name='gallery')

    def __str__(self):
        return self.title
