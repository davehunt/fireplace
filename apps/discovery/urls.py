from django.conf.urls.defaults import patterns, url, include

from addons.urls import ADDON_ID
from . import views


# These will all start with /addon/<addon_id>/
addon_patterns = patterns('',
    url('^$', views.addon_detail, name='discovery.addons.detail'),
    url('^eula/(?P<file_id>\d+)?$', views.addon_eula,
        name='discovery.addons.eula'),
)


urlpatterns = patterns('',
    url('^addon/%s/' % ADDON_ID, include(addon_patterns)),

    url('^recs$', views.recommendations, name='discovery.recs'),
    url('^(?P<version>[^/]+)/(?P<platform>[^/]+)$', views.pane,
        name='discovery.pane'),
    url('^modules$', views.module_admin, name='discovery.module_admin'),
)
