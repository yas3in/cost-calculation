from django.db import models
from django.contrib.auth.models import User

class Calculater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=9, decimal_places=0)
    description = models.TextField(null=True, blank=True)
