# Create your views here.
from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm

def my_view(request):
	# Just display a template
	template_name = 'my_view.html'

	return render(request, template_name, {})
def quote_list(request):
	template_name = 'quotemeonthat/list.html'
	my_quotes = Quote.objects.filter(active=True)

	return render(request, template_name, {'quotes': my_quotes})
def quote_detail(request, pk):
	template_name = 'quotemeonthat/detail.html'
	this_contact = Quote.objects.get(pk=pk)

	return render(request, template_name, {'quote': this_contact})
def quote_add(request):
	template_name = 'quotemeonthat/add.html'
	saved = False

	if request.method == 'POST':
		form = QuoteForm(request.POST)
		if form.is_valid():
			form.save()
			saved = True
		else:
			form = QuoteForm()

		return render(request, template_name, {
			'form': form,
			'saved':saved,
			})