from django.conf.urls import url

from notes.views import entry_list, entry_detail, entry_create

urlpatterns = [
    url(r'^$', entry_list),
    url(r'^create/$', entry_create),
    url(r'^(?P<id>\d+)/$', entry_detail)

]
