from django.urls import path
from calculation import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calculater/', views.calculater, name='calculater'),
    path('insert-data/', views.insert_data, name='insert-data'),
    path('user-panel/', views.user_panel, name='user-panel'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('test/', views.test, name='test'),
    path('chart/', views.chart, name='chart'),
    path('help/', views.help, name='help'),
    path('user-information/', views.user_information, name='user-information'),
    path('exit/', views.user_information, name='exit'),
    path('poshtibani/', views.poshtibani, name='poshtibani'),
    path('update_user/', views.update_user, name='update_user'),
]
