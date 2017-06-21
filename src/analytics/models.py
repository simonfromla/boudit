from django.db import models

# Create your models here.
from shortener.models import ShawtyURL


class ClickEventManager(models.Manager):
    def create_event(self, shawtyInstance):
        if isinstance(shawtyInstance, ShawtyURL):
            obj, created = self.get_or_create(shawty_url=shawtyInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    shawty_url    = models.OneToOneField(ShawtyURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)