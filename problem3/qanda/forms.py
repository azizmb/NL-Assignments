from django import forms

from models import Question, Answer

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        
class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        