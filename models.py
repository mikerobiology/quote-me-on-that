from django import models

class Quote(models.model):
  catalog_number = models.CharField(max_length=100)
	item_description = models.CharField(max_length=100)
	vendor = models.CharField(max_length=100)
	quote_number = models.CharField(max_length=100)
	quote_expires = models.DateField()
	
