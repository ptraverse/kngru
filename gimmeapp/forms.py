
from django import forms 
class PostForm(forms.Form):
	element_1 = forms.CharField(max_length=100)
	element_2 = forms.CharField()
 	description  = forms.CharField()
	 # # # # price = forms.FloatField()
	# def is_valid(self):
		
