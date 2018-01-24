from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import EntryModelForm
from .models import Entry

def entry_list(request):
	entries = Entry.objects.all()
	context = {
		'object_list': entries
	}
	return render(request, "notes/entries.html", context)


def entry_detail(request, id):
	note = get_object_or_404(Entry, id=id)
	context = {
		'object': note
	}
	return render(request, "notes/entries_detail.html", context)


def entry_create(request):
	form = EntryModelForm(request.POST or None)
	if form.is_valid():
		print(form)
	context = {
		'form': form
	}

	return render(request, "notes/entries_create.html", context)


#CRUD

#CREATE
#RETRIEVE / DETAIL
#UPDATE
#DELETE

#LIST