from django.urls import path
from calculation.views import index, calculater, show_data, insert_data


urlpatterns = [
    path('', index, name='index'),
    path('calculater/', calculater, name='calculater'),
    path('insert-data/', insert_data, name='insert-data'),
    path('show-data/', show_data, name='show-data'),
]
