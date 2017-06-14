from django.db import models
import random
import string

from shortener.utils import create_unique_code
# Create your models here.

class ShawtyURLManager(models.Manager):
    # To use this model manager, it must be linked to the model. Set the 'objects' field in ShawtyURL for use through queries
    def all(self, *args, **kwargs):
        print("im here")
        qs = super(ShawtyURLManager, self).all(*args, **kwargs).filter(active=True)
        return qs

    def refresh_codes(self, items=None):

        qs = ShawtyURL.objects.filter(id__gte=1)

        print('Management Command Argument Passed: \'{i}\''.format(i=items))

        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        """If items param is passed on management command, then reverse the list of objects, and return up to the 'items' number passed.

        Reverses list in order to return the most recent number of 'items' results
        """

        new_code_count = 0
        for q in qs:
            q.shortcode = create_unique_code(q)
            q.save()
            print(q.id, q.shortcode)
            new_code_count += 1

        return "New codes: {i}".format(i=new_code_count)



class ShawtyURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20, unique=True, blank=True)
    #shortcode = models.CharField(max_length=20, null=True) null=True: Empty in db is OK
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    #A way to set the datetime yourself in the admin gui. Note: auto_=False
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = ShawtyURLManager()


    def save(self, *args, **kwargs):
        #Add changes to default save() method here:
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_unique_code(self)
        super(ShawtyURL, self).save(*args, **kwargs)

        # Modifying the default .save() method to also change the shortcode to a randomly generated one

    # Change the ordering directly on the qs, as done on refresh_codes(), or change the default ordering here:
    # class Meta:
    #     ordering = '-id'

    def __str__(self):
        return str(self.url)


