from django import forms
from calculation.models import Calculater


class GetDataForm(forms.Form):
    cost = forms.DecimalField(max_digits=9, decimal_places=0, widget=forms.TextInput(attrs={'placeholder': 'هزینه ات رو اینجا وارد کن'}))
    description = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'توضیحات هزینه'}))
    date = forms.DateField()
    