from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('dataapostrophe.artwork.views',
    (r'^$', 'index')
)
