from django.conf.urls import url

from . import views

# Here is a URLconf 

"""
#v1
# add a namespace
app_name = 'polls'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^$', views.hgDemo, name='hgDemo'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
"""

# v2
app_name = 'polls'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

