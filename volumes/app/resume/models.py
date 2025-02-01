from django.db import models


# Create your models here.
class Summary(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300, default='description')
    short_description = models.TextField(
        max_length=300, default='short description')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    from_date = models.DateField(null=True, blank=True)
    till_date = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=300, default='description')

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=255)
    from_date = models.DateField(null=True, blank=True)
    till_date = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    university_location = models.CharField(max_length=255)
    description = models.TextField(max_length=300, default='description')

    def __str__(self):
        return self.title
