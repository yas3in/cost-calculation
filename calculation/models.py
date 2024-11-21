from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count, Q


class Calculater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=9, decimal_places=0)
    description = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.user} {self.cost}"
    

class CostBalance(models.Model):
    user = models.ForeignKey(User, related_name="transactions", on_delete=models.RESTRICT)
    cost = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)


    @classmethod
    def balance(cls, user):
        """
        transaction it`s related name`s Transction model to User model
        
        """

        positive_transaction = Sum("cost")
        
        user_balance = user.transactions.all().aggregate(
        balance=Coalesce(positive_transaction, 0)
            )
        
        return user_balance
    
    
    @classmethod
    def create_instance_in_table(cls, user):
        instance = cls.objects.create(user=user, balance=CostBalance.balance['balance'])
        return instance
        
        
    @classmethod
    def create_record_in_table(cls):
        for user in User.objects.all():
            record = cls.create_instance_in_table(user)
            
            
    def __str__(self) -> str:
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"