from django import forms
from calculation.models import Calculater
from django.contrib.auth.models import User
from django_jalali import forms as jforms
import jdatetime


class GetDataForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "هزینه به تومان وارد کن"}), required=True)
    description = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'دلیل خرجتو کوتاه بنویس'}))
    date = jforms.jDateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'تاریخ خرج مثل:01-02-1403'}))

    
    def save(self):
        calculater = Calculater.add(
            user=self.cleaned_data.get('user'),
            cost=self.cleaned_data.get('cost'),
            description=self.cleaned_data.get('description'),
            date=self.cleaned_data.get('date')
        )
        return calculater
