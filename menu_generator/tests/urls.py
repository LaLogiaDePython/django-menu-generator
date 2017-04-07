from django.conf.urls import url

urlpatterns = [
    url('', lambda: 'foo'),
    url('named-url', lambda: 'foo', name='named_url'),
    url('named-with-params/(?P<pk>\d+)/', lambda: 'foo', name='named_with_params')
]
