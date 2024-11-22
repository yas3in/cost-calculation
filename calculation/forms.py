from django import forms
from calculation.models import Calculater
from django_jalali import forms as jforms
import jdatetime


class GetDataForm(forms.Form):
    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'هزینه ات رو اینجا وارد کن'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'توضیحات هزینه'}), required=False)
    date = jforms.jDateField()

    
    def save(self, user):
        calculater = Calculater.add(
            user=user,
            cost=self.cleaned_data.get('cost'),
            description=self.cleaned_data.get('description'),
            date=self.cleaned_data.get('date')
        )
        return calculater
