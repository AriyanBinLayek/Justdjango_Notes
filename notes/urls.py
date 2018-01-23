from django.conf.urls import url

from notes.views import entry_list, entry_detail

urlpatterns = [
    url(r'^$', entry_list),
    url(r'^(?P<id>\d+)/$', entry_detail)
]
