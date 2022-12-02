from django import forms
from .models import *

class AddtoCartForm(forms.Form):
    quantity = forms.IntegerField()
