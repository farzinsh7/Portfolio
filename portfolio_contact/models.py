from django.db import models


class ContactUS(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    is_read = models.BooleanField(verbose_name='is read / unread', default=False)

    def __str__(self):
        return self.full_name
