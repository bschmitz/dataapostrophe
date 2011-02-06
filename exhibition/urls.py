from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('dataapostrophe.exhibition.views',
    (r'^/exhibition$', 'index')
)
