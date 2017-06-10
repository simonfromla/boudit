from django.db import models

# Create your models here.

class ShawtyURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20, unique=True)
    #shortcode = models.CharField(max_length=20, null=True) null=True: Empty in db is OK
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #A way to set the datetime yourself in the admin gui. Note: auto_=False
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return str(self.url)
