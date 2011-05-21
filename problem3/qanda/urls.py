from django.conf.urls.defaults import *
from models import Answer, Question

urlpatterns = patterns('qanda.views',
    url(r'^$', 'landing_page', name="landing_page"),
    url(r'^question/(?P<qid>\w+)', 'question', name="question_page"),
    url(r'^rating/answer', 'rating', {'model': Answer}, name="answer_rating"),
    url(r'^rating/question', 'rating', {'model': Question}, name="question_rating"),
)
