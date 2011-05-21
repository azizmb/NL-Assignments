from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import QuestionForm

def question(request, qid):
    pass

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