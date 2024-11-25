from django.urls import path
from calculation.views import index, calculater, user_panel, insert_data, logs, login_page


urlpatterns = [
    path('', index, name='index'),
    path('calculater/', calculater, name='calculater'),
    path('insert-data/', insert_data, name='insert-data'),
    path('user-panel/', user_panel, name='user-panel'),
    path('logs/', logs, name='logs'),
    path('login/', login_page, name='login'),
]
