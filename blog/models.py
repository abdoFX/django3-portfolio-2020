from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=100)
    title_url = models.URLField(blank=True)
    date = models.DateField
    description = models.CharField(max_length=200)
