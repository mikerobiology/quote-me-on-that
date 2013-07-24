from django.db import models
import datetime

# Create your models here.
class Quote(models.Model):
	catalog_number = models.CharField(max_length=100)
	item_description = models.CharField(max_length=100)
	vendor = models.CharField(max_length=100)
	quote_number = models.CharField(max_length=100)
	quote_expires = models.DateField()
	#Find a way to make this DateField smart?  Allow expired quotes?
	active = models.BooleanField(default=True)
