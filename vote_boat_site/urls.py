from django.conf.urls import patterns, include, url
from django.contrib import admin
from vote_boat_site import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vote_boat_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^create/',views.new_poll,name='create_poll'),
    url(r'^ideas/$',views.poll_urls,name='view_polls'),
    url(r'^ideas/(?P<poll_ideas_url>\w+\-\d*)/$', views.ideas, name='ideas'), 
)
