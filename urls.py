from django.conf.urls.defaults import patterns, include, url

from tastypie.api import Api
from api.resources import PollResource, ChoiceResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yasu.views.home', name='home'),
    # url(r'^yasu/', include('yasu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^polls/(?P<poll_id>\d+)/export/$', 'polls.views.export'),
    
    (r'^api/', include(v1_api.urls)),
)
