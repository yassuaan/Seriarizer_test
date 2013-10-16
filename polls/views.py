# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from polls.models import Choice,Poll

import csv

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))
    
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p},
                               context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
       selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
       return render_to_response('polls/detail.html', {
           'poll': p,
           'error_message': "not choice",
       }, context_instance=RequestContext(request))
    else:
       selected_choice.votes += 1
       selected_choice.save()
       
       return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
    
def export(request, poll_id):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=somefilename.csv'
    
    p = get_object_or_404(Poll, pk=poll_id)
    
    aa = p.choice_set.all
    #for choicea in p.choice_set.all
    #    bb = choicea.choice
    
    return HttpResponse("You're looking at poll %s." % bb)
    #return render_to_response('polls/export.html', {'poll': p})
    
    writer = csv.writer(response)
    
    #for choicea in p.choice_set.all
    #    write.writerow([choicea.choice, choicea.votes])
    
    #writer = csv.writer(response)
    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response
    