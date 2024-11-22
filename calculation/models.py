from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count, Q
from django_jalali.db import models as jmodels
import jdatetime


class Calculater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    cost = models.BigIntegerField()
    description = models.TextField(null=True, blank=True)
    date = jmodels.jDateField()

 
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
 