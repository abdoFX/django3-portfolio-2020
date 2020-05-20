from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=200)
    title_url = models.URLField(blank=True)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title