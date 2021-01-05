from django.conf.urls import url

def testview(request):
    return 'foo'

urlpatterns = [
    url(r'named-url', lambda: 'foo', name='named_url'),
    url(r'named-with-params/(?P<pk>\d+)/', lambda: 'foo', name='named_with_params'),
    url(r'known-view', testview, name='known_view'),
    url(r'', lambda: 'foo'),
]
