from django.db import models

# Create your models here.

class StoredImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')
    img_feature_path = models.TextField()
    def __str__(self):
        return self.name;

class UploadedImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/uploaded')
    img_feature_path = models.TextField()
    def __str__(self):
        return self.name;

