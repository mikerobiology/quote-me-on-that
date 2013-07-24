from django import forms
from quotemeonthat.models import Quote

class QuoteForm(forms.ModelForm):
	class Meta:
		model = Quote
		exclude = ['active']