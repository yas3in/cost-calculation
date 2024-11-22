from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count, Q
from django_jalali.db import models as jmodels


class Calculater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date = jmodels.jDateField()
    cost = models.DecimalField(max_digits=9, decimal_places=0)
    description = models.TextField(null=True, blank=True)

 