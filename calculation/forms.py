from django import forms
from calculation.models import Calculater
from django_jalali import forms as jforms


class GetDataForm(forms.Form):
    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'هزینه ات رو اینجا وارد کن'}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'توضیحات هزینه'}), required=False)
    date = jforms.jDateField(required=False)

    
    def save(self, user):
        calculater = Calculater.add(
            user=user,
            cost=self.cleaned_data.get('cost'),
            description=self.cleaned_data.get('description'),
            date=self.cleaned_data.get('date')
        )
        return calculater
