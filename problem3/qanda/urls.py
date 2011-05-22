from django.conf.urls.defaults import *
from models import Answer, Question

urlpatterns = patterns('qanda.views',
    url(r'^$', 'landing_page', name="landing_page"),
    url(r'^question/(?P<qid>\w+)', 'question', name="question_page"),
    url(r'^rating/answer', 'rating', {'model': Answer}, name="answer_rating"),
    url(r'^rating/question', 'rating', {'model': Question}, name="question_rating"),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
                    )