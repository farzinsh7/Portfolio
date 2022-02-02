from django.db import models


def upload_image_path(instance, filename):
    final_name = f"{instance.id}-{instance.siteTitle}"
    return f"setting/{final_name}"


# Create your models here.
class SiteSetting(models.Model):
    siteTitle = models.CharField(max_length=150)
    about_me = models.TextField(null=True, blank=True)
    logo_image = models.ImageField(upload_to=upload_image_path, null=True)
    fav_icon = models.ImageField(upload_to=upload_image_path, null=True)
    address = models.CharField(max_length=400)
    mobile = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    happy_client = models.IntegerField(null=True)
    projects_count = models.IntegerField(null=True)
    hours_of_support = models.IntegerField(null=True)
    awards = models.IntegerField(null=True)

    def __str__(self):
        return self.siteTitle
