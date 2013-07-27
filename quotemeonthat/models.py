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
	# This does not work.  Site works, but does not auto-select active
	# based on date.  FIGURE THIS OUT.
	def expired(self):
		today = datetime.date.today()
		if self.quote_expires and self.quote_expires < today:
			return False
		if self.quote_expires and self.quote_expires > today:
			return True
	expired = models.BooleanField()
	
	# This might work?  Maybe?
	# active = models.BooleanField(default=True)
	# def expired(self): #need to make sure this works
	#	today = datetime.date.today()
	#	if self.quote_expires and self.quote_expires < today:
	#		active=False
