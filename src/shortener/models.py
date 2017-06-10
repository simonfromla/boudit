from django.db import models
import random
import string

# Create your models here.

def generate_short_on_save(size=7, chars=string.ascii_lowercase + string.digits):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code

class ShawtyURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20, unique=True)
    #shortcode = models.CharField(max_length=20, null=True) null=True: Empty in db is OK
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #A way to set the datetime yourself in the admin gui. Note: auto_=False
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        #Add changes to default save() method here:
        self.shortcode = generate_short_on_save()
        super(ShawtyURL, self).save(*args, **kwargs)

        # Modifying the default .save() method to also change the shortcode to a randomly generated one

    def __str__(self):
        return str(self.url)
