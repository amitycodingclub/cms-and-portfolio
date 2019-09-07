from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Date = models.DateTimeField()
    Image = models.ImageField(upload_to='image/')
    body = models.CharField(max_length=1000)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.Date.strftime('%b %e, %Y')

    def __str__(self):
        return self.Title

class Job(models.Model):
    name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='image/')
    details = models.CharField(max_length=1000)

    def summary(self):
        return self.details[:100]

    def __str__(self):
        return self.Title

