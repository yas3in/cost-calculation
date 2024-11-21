from django.urls import path
from calculation.views import index, calculater


urlpatterns = [
    path('', index, name='index'),
    path('calculater/', calculater, name='calculater')
]
