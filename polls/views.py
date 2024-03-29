from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from polls.models import Poll, Choice

def vote(request, poll_id):
    
    poll = get_object_or_404(Poll, pk=poll_id)
    choice = request.POST['choice']
    try:
        selected_choice = poll.choice_set.get(pk=choice)
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/details.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_results', args=(poll.id,)))
