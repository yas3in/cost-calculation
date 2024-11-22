from django import forms
from calculation.models import Calculater
from django.contrib.auth.models import User
from django_jalali import forms as jforms
import jdatetime


class GetDataForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'هزینه ات رو اینجا وارد کن'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'توضیحات هزینه'}), required=False)
    date = jforms.jDateField(required=True)

    
    def save(self):
        calculater = Calculater.add(
            user=self.cleaned_data.get('user'),
            cost=self.cleaned_data.get('cost'),
            description=self.cleaned_data.get('description'),
            date=self.cleaned_data.get('date')
        )
        return calculater
