from django.db import models

# Create your models here.

class Client(models.Model):
	channel_name =  models.TextField(null=True, blank=True)