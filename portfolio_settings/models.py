from django.db import models



# Create your models here.
class SiteSetting(models.Model):
    siteTitle = models.CharField(max_length=150)
    about_me = models.TextField(null=True, blank=True)
    logo_image = models.ImageField(upload_to="logo", null=True)
    fav_icon = models.ImageField(upload_to="fav-icon", null=True)
    address = models.CharField(max_length=400)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    happy_client = models.IntegerField(null=True)
    projects_count = models.IntegerField(null=True)
    hours_of_support = models.IntegerField(null=True)
    awards = models.IntegerField(null=True)

    def __str__(self):
        return self.siteTitle


class SocialMedias(models.Model):
    title = models.CharField(max_length=120)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    site_setting = models.ForeignKey(SiteSetting, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.title



class MySkills(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Services(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    class_icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title
