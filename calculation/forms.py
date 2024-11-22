from django import forms
from calculation.models import Calculater


class GetDataForm(forms.Form):
    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'هزینه ات رو اینجا وارد کن'}), required=False)
    description = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'توضیحات هزینه'}), required=False)
    date = forms.DateField(required=False)

    
    # def save(self, calculater):
    #     calculater.add(
    #         self.clean_data.get('cost'),
    #         self.clean_data.get('description'),
    #         self.clean_data.get('date')
    #     )
    #     return calculater
