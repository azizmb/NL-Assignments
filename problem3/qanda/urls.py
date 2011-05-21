from django.conf.urls.defaults import *

urlpatterns = patterns('qanda.views',
    url(r'^$', 'landing_page', name="landing_page"),
    url(r'^question/(?P<qid>\w+)', 'question', name="question_page"),
)
