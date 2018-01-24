from django.conf.urls import url

from notes.views import entry_list, entry_detail, entry_create

urlpatterns = [
    url(r'^$', entry_list, name='list'),
    url(r'^create/$', entry_create, name='create'),
    url(r'^(?P<id>\d+)/$', entry_detail, name='detail')

]
