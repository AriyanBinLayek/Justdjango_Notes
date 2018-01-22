from django.shortcuts import render

# Create your views here.
from .models import Entry

def entry_view(request):
	entries = Entry.objects.all()
	context = {
		'object_list': entries
	}
	return render(request, "notes/entries.html", context)