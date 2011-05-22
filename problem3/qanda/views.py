from simplejson import dumps

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse

from forms import QuestionForm, AnswerForm
from models import Question

def rating(request, model):
    pk = request.POST['id']
    
    instance = get_object_or_404(model, pk=pk)
    
    if request.POST['name'] == "up":
	instance.rating += 1
	instance.save()
    elif request.POST['name'] == "down":
	instance.rating -= 1
	instance.save()
    else:
	return HttpResponseBadRequest()
    
    response = HttpResponse(
        content=dumps({"rating": instance.rating}),
        mimetype='application/json'
    )
    return response


def question(request, qid):
    question = get_object_or_404(Question, pk=qid)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
	    instance.question = question
	    instance.save()
	    
    else:
        form = AnswerForm()
        
    form.action = reverse("qanda.views.question", kwargs={'qid': qid})
    
    return render_to_response(
        "qanda/question.html", 
        { 
            "form": form, 
            "question": question 
        }, 
        RequestContext (request)
    )

def landing_page(request):
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            instance = form.save()
	    #return HttpResponseRedirect("qanda.views.question", kwargs={'qid': instance.pk})
    else:
        form = QuestionForm()
        
    form.action = reverse("qanda.views.landing_page")
    
    return render_to_response(
        "qanda/landing.html", 
        { "form": form, }, 
        RequestContext (request)
    )