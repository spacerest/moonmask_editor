from django.db import models

# Create your models here.

def get_upload_path(cls, filename):
    return cls.__class__.__name__ + "/" + filename

class Collage(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to = get_upload_path, null=True, blank=True)
