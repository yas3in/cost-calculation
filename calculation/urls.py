from django.urls import path
from calculation.views import index, calculater, user_panel ,insert_data, signin, login_page, signup, test


urlpatterns = [
    path('', index, name='index'),
    path('calculater/', calculater, name='calculater'),
    path('insert-data/', insert_data, name='insert-data'),
    path('user-panel/', user_panel, name='user-panel'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('test/', test, name='test'),
]
