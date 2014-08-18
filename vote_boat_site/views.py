from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from vote_boat.views import create_new_poll,ideas,poll_urls

def home (request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = dict(message="Welcome to...the Vote Boat!")

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('vote_boat_site/index.html', context_dict, context)

def thank_you (request):
    context = RequestContext(request)
    context_dict = dict(message="Thank You!")
    return render_to_response('vote_boat_site/index.html', context_dict, context)
    
new_poll = create_new_poll('vote_boat_site/new_poll.html',thank_you)



