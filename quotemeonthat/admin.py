from django.contrib import admin
from .models import Quote
class QuoteAdmin(admin.ModelAdmin):
	model = Quote
	list_display = ['vendor', 'quote_number', 'catalog_number', 'item_description']
	search_fields = ['item_description', 'vendor', 'catalog_number', 'quote_number']
	list_display_links = ['item_description', 'vendor', 'catalog_number', 'quote_number']
	ordering = ['item_description', 'vendor', 'quote_number', 'quote_expires']
	list_filter = ['expired']
	# add a list_filter to filter out expired quotes?

admin.site.register(Quote, QuoteAdmin)