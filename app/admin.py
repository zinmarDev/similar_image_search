import imp
from django.contrib import admin

# Register your models here.
from .models import StoredImage, UploadedImage
admin.site.register(StoredImage)
admin.site.register(UploadedImage)