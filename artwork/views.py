from django.shortcuts import render_to_response
from django.template import RequestContext
from dataapostrophe.artwork.models import ArtWork

def index(request):
    page_context = {'artworks': ArtWork.objects.all() }
    template_name = 'artwork/index.html'
    return render_to_response(template_name, page_context,
                                  context_instance = RequestContext(request)) 


