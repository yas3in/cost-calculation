from django.urls import path
from calculation.views import index, calculater, user_panel, insert_data, login


urlpatterns = [
    path('', index, name='index'),
    path('calculater/', calculater, name='calculater'),
    path('insert-data/', insert_data, name='insert-data'),
    path('user-panel/', user_panel, name='user-panel'),
    path('login/', login, name='login'),
]
