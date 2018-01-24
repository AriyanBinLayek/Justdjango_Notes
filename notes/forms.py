from django import forms

from .models import Entry

class EntryForm(forms.Form):
	pass


class EntryModelForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['title', 'description', 'image']