from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count, Q
from django_jalali.db import models as jmodels


class Calculater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date = jmodels.jDateField()
    cost = models.BigIntegerField()
    description = models.TextField(null=True, blank=True)

 
    def __str__(self):
        return f"{self.user} {self.cost}"
    
    
    @classmethod
    def add(cls, user, cost, date, description):
        create = Calculater.objects.create(
            user=user,
            cost=cost,
            date=date,
            description=description
        )
        create.save()
        return create
 
class AllCost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_cost')
    amount = models.BigIntegerField()
    
    
    def users(self):
        user = User.objects.all()
 
    @classmethod
    def costing(cls, users):
        for user in users:
            cal = Calculater.objects.filter(user=user).annotate(sum=Sum('cost'))
            return cal