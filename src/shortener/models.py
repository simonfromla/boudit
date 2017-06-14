from django.db import models
import random
import string

from shortener.utils import generate_shortcode, check_unique_code
# Create your models here.


class ShawtyURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20, unique=True, blank=True)
    #shortcode = models.CharField(max_length=20, null=True) null=True: Empty in db is OK
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #A way to set the datetime yourself in the admin gui. Note: auto_=False
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        #Add changes to default save() method here:
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = check_unique_code(self)
        super(ShawtyURL, self).save(*args, **kwargs)

        # Modifying the default .save() method to also change the shortcode to a randomly generated one

    def __str__(self):
        return str(self.url)
