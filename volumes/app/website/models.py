from django.db import models



# Create your models here.
class MyInformations(models.Model):
    site_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    about_me = models.TextField(null=True, blank=True)
    logo_image = models.ImageField(upload_to="logo", null=True)
    background_image = models.ImageField(upload_to="background", null=True)

    def __str__(self):
        return self.site_title


class SocialMedias(models.Model):
    title = models.CharField(max_length=120)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    site_setting = models.ForeignKey(MyInformations, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.title