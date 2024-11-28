from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from calculation.models import Calculater
from calculation.forms import GetDataForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import pandas as pd
import jdatetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import plotly.express as px


def index(request):
    return render(request, 'index.html')


@login_required
def insert_data(request):
    form = GetDataForm({'date': jdatetime.date.today(), 'user': request.user})
    if form.is_valid() is not None:
        form.save()
        return render(request, 'calculater.html', {'form': form})
    else:
        return Http404
    
 
@require_POST
@login_required
def calculater(request):
    form = GetDataForm(request.POST)
    if form.is_valid() is not None:
        form.save()
    response = request.POST.get('next', '/')
    return HttpResponseRedirect(response)
    
 
def user_panel(request):
    if request.user.is_authenticated:
        recently = Calculater.recently_cost(request)
        variable_cost = Calculater.variable_cost(request)
        return render(request, 'user_panel.html', 
                            {'recently': recently, 'least_cost': variable_cost['least_cost'], 
                             'more_cost': variable_cost['more_cost'], 'costs': variable_cost['sum_cost']})
    else:
        return redirect('login')
    
    
@require_POST
def signin(request):
    response = HttpResponseRedirect(request.POST.get('next', '/'))

    next = request.POST.get('next')
    
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next.endswith('login/'):
            return redirect('user-panel')
        else:
            return response
    else:
        return redirect('login')


@require_POST
def signup(request):
    response = HttpResponseRedirect(request.POST.get('next', '/'))
    next = request.POST.get('next')
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    if username and username and username is not None:
        sign_up = Calculater.create_user(username, email, password)
        if sign_up:
            user = authenticate(request, username=username, password=password)
            login(request, user)
            if next.endswith('login/'):
                return redirect('user-panel')
            else:
                return response
        else:
            return redirect('login')
    else:
        return Http404

        
def login_page(request):
    if request.user.is_authenticated:
        return redirect('user-panel')
    else:
        return render(request, 'login.html')

def test(request):
    if request.user.is_authenticated:
        chart_html = Calculater.monthly_cost(request)
        return render(request, 'test.html', 
                            {'monthly': chart_html})
    else:
        return redirect('login')
    

@login_required
def user_information(request):
    return render(request, 'user_information.html')


def poshtibani(request):
    return render(request, 'poshtibani.html')


def help(request):
    pass


@login_required
def exit(request):
    pass


@login_required
def chart(request):
    pass
    

@login_required
@require_POST
def update_user(request):
    u = User.objects.get(username=request.user)
    u.first_name = request.POST.get("firstname")
    u.last_name = request.POST.get("lastname")
    u.save()
    return redirect('user-information')
