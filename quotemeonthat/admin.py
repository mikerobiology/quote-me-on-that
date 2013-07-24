from django.contrib import admin
from .models import Quote
class QuoteAdmin(admin.ModelAdmin):
	model = Quote
	list_display = ['item_description', 'vendor', 'quote_number']
	search_fields = ['item_description', 'vendor', 'catalog_number']
	list_display_links = ['item_description', 'vendor']
	ordering = ['quote_expires', 'item_description']
	# add a list_filter to filter out expired quotes?

admin.site.register(Quote, QuoteAdmin)