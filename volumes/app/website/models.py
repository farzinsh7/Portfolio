from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from colorfield.fields import ColorField


# Create your models here.
class Website(models.Model):
    site_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    about_me = models.TextField(null=True, blank=True)
    logo_image = models.ImageField(upload_to="logo", null=True)
    background_image = models.ImageField(upload_to="background", null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_title


class SocialMedias(models.Model):
    title = models.CharField(max_length=120)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200, blank=True, null=True)
    socials = models.ForeignKey(
        Website, null=True, on_delete=models.SET_NULL, related_name='socials')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MyInformation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='description')
    image = models.ImageField(upload_to="photo")
    birth_date = models.DateField()
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    email = models.EmailField()
    freelance = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0, validators=[
                                MinValueValidator(0), MaxValueValidator(100)])
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Counter(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(null=True)
    icon = models.CharField(max_length=50)
    counter = models.ForeignKey(
        MyInformation, null=True, on_delete=models.SET_NULL, related_name='counter')

    def __str__(self):
        return self.title


class InterestedIn(models.Model):
    title = models.CharField(max_length=50)
    color = ColorField(default='#FF0000')
    icon = models.CharField(max_length=50)
    interested = models.ForeignKey(
        MyInformation, null=True, on_delete=models.SET_NULL, related_name='interested')

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    full_name = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.full_name}"
