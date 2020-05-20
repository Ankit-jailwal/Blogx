from django.db import models

class blogpost(models.Model):
    title = models.TextField()
    content=models.TextField(null=True, blank=True )