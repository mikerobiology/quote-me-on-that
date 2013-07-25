from django.db import models
from decimal import Decimal
import datetime

class Quote(models.Model):
	quote_number = models.CharField(max_length=100)
	catalog_number = models.CharField(max_length=100)
	item_description = models.CharField(max_length=100)
	vendor = models.CharField(max_length=100)
	list_price = models.DecimalField(max_digits=100, decimal_places=2,
		null=True)
	discount = models.DecimalField(max_digits=100, decimal_places=2,
		null=True)
	net_price = models.DecimalField(max_digits=100, decimal_places=2,
		null=True)
	quote_expires = models.DateField()
	#Find a way to make this DateField smart?  Allow expired quotes?
	active = models.BooleanField(default=True)
