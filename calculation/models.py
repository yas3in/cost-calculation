from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
import jdatetime
import pandas as pd
import plotly.express as px


class Calculater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    cost = models.BigIntegerField()
    description = models.TextField(null=True, blank=True, max_length=30)
    date = jmodels.jDateField()

 
    def __str__(self):
        return f"{self.user} {self.cost}"
    
    
    @classmethod
    def add(cls, user, cost, date, description):
        if user and cost:
            if date is None:
                date = jdatetime.date.today()
            create = Calculater.objects.create(
                user=user,
                cost=cost,
                date=date,
                description=description
            )
            create.save()
            return create
 
 
    @classmethod
    def create_user(cls, username, email, password):
        try:
            User.objects.create_user(username, email, password)
            return True
        except:
            return False
        
    
    def recently_cost(request):
        try:
            dt = Calculater.objects.filter(user=request.user).values().order_by('-date', '-id')[:5]
            data = pd.DataFrame(dt)
            data = data.rename(columns={
                "cost": "هزینه",
                "date": "تاریخ",
                "description": "توضیح خرید"
            })
            data['هزینه'] = data['هزینه'].apply(lambda x: f"{x:,.0f} تومان")
            data = data.to_html(columns=['هزینه', 'تاریخ', "توضیح خرید"], 
                            col_space=5, index=False,
                            justify='center'
                            )
            return data
        except:
            return " "
        
        
    def monthly_cost(request):
        month = jdatetime.date.today()
        data = Calculater.objects.filter(user=request.user).values()
        df = pd.DataFrame(data)

        # تبدیل تاریخ شمسی به میلادی برای عملیات فیلتر
        df['GregorianDate'] = df['date'].apply(lambda x: x.togregorian())

        # تبدیل به datetime میلادی
        df['GregorianDate'] = pd.to_datetime(df['GregorianDate'])
        df['date'] = df['GregorianDate'].dt.month == month.month

        # تبدیل تاریخ میلادی فیلتر شده به شمسی برای نمایش
        df['date'] = df['GregorianDate'].apply(lambda x: jdatetime.datetime.fromgregorian(datetime=x))
        df['cost'] = df['cost'].apply(lambda x: f"{x:,.0f} تومان")
        
        fig = px.bar(y=df['date'], x=df['cost'], title="هزینه های ماه جاری")
        fig.update_yaxes(title="date", tickformat="%Y-%m-%d")
        chart_html = fig.to_html(full_html=False)
        return chart_html


    def variable_cost(request):
        data = Calculater.objects.filter(user=request.user).values()
        df = pd.DataFrame(data)
        costs = df['cost'].sum()
        more_cost = df['cost'].max()
        least_cost = df['cost'].min()
        costs = f"{costs:,}"
        least_cost = f"{least_cost:,}"
        more_cost = f"{more_cost:,}"
        return {'sum_cost': costs, 'more_cost': more_cost, 'least_cost': least_cost}
    
    
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket")
    ticket_type = models.CharField(max_length=30)
    ticket = models.TextField()
    
    
    def __str__(self):
        return f"{self.user} {self.ticket} {self.ticket_type}"
    
    
    @classmethod
    def add(cls, user, ticket_type, ticket):
        object = Ticket.objects.create(
            user=user, ticket_type=ticket_type, ticket=ticket
            )
        object.save()
        return object


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomme")
    income = models.BigIntegerField()
    purpose = models.CharField(max_length=48, default=" ")
    lateral = models.BigIntegerField(null=True, blank=True)
    date = jmodels.jDateField()
    
    
    def __str__(self):
        return f"{self.user} - {self.income}"
    
    
    @classmethod
    def add(cls, user, income, purpose, lateral, date):
        if date is None:
            date = jdatetime.date.today()
            object = Income.objects.create(
                user=user,
                income=income,
                purpose=purpose,
                lateral=lateral,
                date=date
            )
            object.save()
            return object
