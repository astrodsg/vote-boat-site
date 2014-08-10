from django.conf.urls import patterns, include, url
from django.contrib import admin
from vote_boat_site import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vote_boat_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^new_poll/',views.new_poll,name='new_poll')
)
