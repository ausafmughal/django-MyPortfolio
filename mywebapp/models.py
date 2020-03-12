from django.db import models
import datetime
class posts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100, default='Ausaf Liaquat')
    image = models.ImageField(upload_to='mywebapp/img/')
    date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title