from django import forms

class Writing(forms.Form):
	content = forms.CharField(label=False, widget=forms.Textarea(attrs={'class' : 'form-control'}))