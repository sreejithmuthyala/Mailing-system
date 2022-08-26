from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Sentreceive(models.Model):

    username= models.CharField(max_length=100)
    # sent_mails= ArrayField(models.TextField())
    # receive_mails=ArrayField(ArrayField(models.TextField()))
    # the_json_sent = models.JSONField(blank=True, null=True)
    rm = ArrayField(ArrayField(ArrayField(models.TextField())))
    sm = ArrayField(ArrayField(ArrayField(models.TextField())))