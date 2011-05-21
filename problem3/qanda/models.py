from django.db import models

class PostModel(models.Model):
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    
    class Meta:
        abstract = True
    
class Question(PostModel):
    question = models.TextField(max_length=100)
    
    
class Answer(PostModel):
    question = models.ForeignKey("Question")
    answer = models.TextField(max_length=100)
    