from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^problem/$', 'django.views.generic.simple.direct_to_template', {'template': 'problem_statement.html'}, name="problem_statement"),
    url(r'^', include("qanda.urls")),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
                    )