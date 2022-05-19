from django.db import models
import datetime
import os

# Create your models here.

def filepath(request, filename):
    old_filename = filename.split('.')
    timeNow = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = old_filename[0] + timeNow + '.jpg'
    return os.path.join('uploads/', filename)

class BlogModel(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    blogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title
    