from django.db import models


class ServicesSummary(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    services = models.ForeignKey(
        ServicesSummary, null=True, on_delete=models.SET_NULL, related_name='services')

    def __str__(self):
        return self.title
