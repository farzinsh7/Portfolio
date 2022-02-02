from django.db import models


class MySkills(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.title

