from django.db import models

# Create your models here.

class Contact(models.Model):
    srno = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    phNo = models.CharField(max_length=13)
    query = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
    