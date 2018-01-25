from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .forms import EntryModelForm
from .models import Entry


def entry_list(request):
	entries = Entry.objects.filter(user=request.user)
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
	form = EntryModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		entry_id = form.instance.id
		entry = get_object_or_404(Entry, id=entry_id)
		messages.info(request, 'Created a New Note.')
		return redirect(entry.get_absolute_url())
	context = {
		'form': form
	}

	return render(request, "notes/entries_create.html", context)


def entry_update(request, id):
	instance = get_object_or_404(Entry, id=id)
	form = EntryModelForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		form.save()
		entry_id = form.instance.id
		entry = get_object_or_404(Entry, id=entry_id)
		return redirect(entry.get_absolute_url())
	context = {
		'form': form,
		'instance': 'object'
	}

	return render(request, "notes/entries_update.html", context)		


def entry_delete(request, id):
	entry = get_object_or_404(Entry, id=id)
	if entry.user != request.user:
		response = HttpResponse("You don't have permission to delete this note.")
		response.status_code = 403
		return response

	if request.method == "POST":
		entry.delete()
		messages.info(request, "This note has been successfully deleted.")
		return redirect("/entries/")

	context = {
		'object': entry
	}
	return render(request, "notes/entries_delete.html", context)
