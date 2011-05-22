from django.conf.urls.defaults import *
from models import Answer, Question
from feeds import LatestQuestionsFeed

urlpatterns = patterns('qanda.views',
    url(r'^$', 'landing_page', name="landing_page"),
    url(r'^question/(?P<qid>\w+)', 'question', name="question_page"),
    
    url(r'^rating/answer', 'rating', {'model': Answer}, name="answer_rating"),
    url(r'^rating/question', 'rating', {'model': Question}, name="question_rating"),
    
    url(r'^recent/answer', 'recent', {'model': Answer}, name="answer_recent"),
    url(r'^recent/question', 'recent', {'model': Question}, name="question_recent"),
    
    url(r'^feed/question', LatestQuestionsFeed(), name="question_feed"),    
)

urlpatterns += (
    url(r'^questions/$', 'django.views.generic.list_detail.object_list', {'queryset':Question.objects.all()}, name="question_list"),
)