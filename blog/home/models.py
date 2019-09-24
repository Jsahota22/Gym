from django.db import models

# Create your models here.
class Reviews(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


