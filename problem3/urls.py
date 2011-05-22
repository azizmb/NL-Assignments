from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include("qanda.urls")),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
                    )