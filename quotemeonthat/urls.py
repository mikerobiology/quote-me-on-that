from django.conf.urls.defaults import *

from .views import my_view, quote_list, quote_detail, quote_add

urlpatterns = patterns('',
	url(r'^myview/$', my_view, name='my_view'),
	url(r'^list/$', quote_list, name='quote-list'),
	url(r'^detail/(?P<pk>\d+)/$', quote_detail, name='quote-detail'),
	url(r'^add/$', quote_add, name='quote-add'),
)