from django import forms
from calculation.models import Calculater, Ticket, Income
from django.contrib.auth.models import User
from django_jalali import forms as jforms
import jdatetime


class GetDataForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "هزینه به تومان وارد کن"}), required=True)
    description = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'دلیل خرجتو کوتاه بنویس'}))
    date = jforms.jDateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'تاریخ خرج مثل:01-02-1403', 'class': 'input-date'}))

    
    def save(self):
        calculater = Calculater.add(
            user=self.cleaned_data.get('user'),
            cost=self.cleaned_data.get('cost'),
            description=self.cleaned_data.get('description'),
            date=self.cleaned_data.get('date')
        )
        return calculater
    
    
class CreateTicketForm(forms.Form):
    TYPES = (
        ("none", " "),
        ("technical", "اشکالات فنی"),
        ("finance", "اشکالات مالی"),
        ("bug", "اختلال یا باگ"),
        ("other", "اشکالات دیگر")
    )
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    ticket_type = forms.ChoiceField(choices=TYPES, widget=forms.Select(attrs={'class': 'ticket_type'}), label="دلیل تیک شما چیست؟")
    ticket = forms.CharField(widget=forms.TextInput(attrs={'class': 'ticket'}), label="متن تیکت خود را بنویسید.")


    def save(self):
        ticket = Ticket.add(
            user=self.cleaned_data.get('user'),
            ticket=self.cleaned_data.get('ticket'),
            ticket_type=self.cleaned_data.get('ticket_type')
        )
        return ticket
    
    
class IncomeForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    income = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "درآمد ثابتت چقدره؟", 'class': 'income'}), required=True)
    purpose = forms.CharField(widget=forms.TextInput(attrs={'class': 'ticket'}), label="یک هدف رو ثبت کن تا کمکت کنم بهش برسی")
    lateral = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "به تومان"}), label="اگه درآمد جانبی هم داری وارد کن", required=False)
    
    
    def save(self):
        income = Income.add(
            user=self.cleaned_data.get('user'),
            income=self.cleaned_data.get('income'),
            purpose=self.cleaned_data.get('purpose'),
            lateral=self.cleaned_data.get('lateral')
        )
        return income