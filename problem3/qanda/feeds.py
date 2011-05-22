from django.contrib.syndication.views import Feed
from models import Question

class LatestQuestionsFeed(Feed):
    title = "QandA - Questions"
    link = "/questions/"
    description = "Latest questions posted on QandA."

    def items(self):
        return Question.objects.order_by('-posted_on')[:5]

    def item_title(self, item):
        return item.question

    def item_description(self, item):
        return "%s\nPosted By: %s"%(item.question, item.posted_by)

