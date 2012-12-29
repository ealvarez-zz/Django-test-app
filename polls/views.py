from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from polls.models import Poll


def index(request):
    latest_polls = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.djhtml', {'latest_polls' : latest_polls})

def details(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/details.djhtml', {'poll':poll})
    
def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)