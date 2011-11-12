from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def index(request):
    return HttpResponse("Hello World!")

def date(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s</html></body>" % now
    return HttpResponse(html)
def head_hour(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()       
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s),it will be %s.</body></html>" %(offset, dt)
    return HttpResponse(html)

    
def current_time(request):
    now = datetime.datetime.now()

    return render_to_response('current_time.html',{'current_time':now})

def base(request):
	return render_to_response('base.html')

def show_note(request):
	return render_to_response('show_note.html')

def add_note(request):
	return render_to_response('add_note.html')
