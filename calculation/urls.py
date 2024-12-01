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
    path('exit/', views.exit, name='exit'),
    path('exit_view/', views.exit_view, name='exit_view'),
    path('poshtibani/', views.poshtibani, name='poshtibani'),
    path('update_user/', views.update_user, name='update_user'),
    path('ticket/', views.ticket, name='ticket'),
    path('income/', views.income, name='income'),
    path('income-view/', views.income_view, name='income-view'),
]
