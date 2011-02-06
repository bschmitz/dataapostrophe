from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    page_context = {'Hello': 'world'}
    template_name = 'exhibition/index.html'
    return render_to_response(template_name, page_context,
                                  context_instance = RequestContext(request)) 


