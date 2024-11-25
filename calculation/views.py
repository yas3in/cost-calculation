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


def index(request):
    return render(request, 'index.html')


@login_required
def insert_data(request):
    form = GetDataForm({'date': jdatetime.date.today(), 'user': request.user})
    if form.is_valid() is not None:
        form.save()
        print(request.POST)
        return render(request, 'calculater.html', {'form': form})
        return redirect
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
        # user = User.objects.filter(user=request.user)
        dt = Calculater.objects.filter(user=request.user).values().order_by('-date', '-id')[:5]
        data = pd.DataFrame(dt)
        data = data.rename(columns={
            "cost": "هزینه",
            "date": "تاریخ",
            "description": "توضیح خرید"
        })
        data['هزینه'] = data['هزینه'].apply(lambda x: f"{x:,.0f} تومان")
        return render(request, 'user_panel.html', 
                        {
                            'data': data.to_html(
                                columns=['هزینه', 'تاریخ', "توضیح خرید"], 
                                col_space=5, index=False,
                                justify='center', border=None
                            )
                        }
                    )
    else:
        return redirect('login')
    
    
@require_POST
def logs(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next.endswith('login/'):
                return redirect('user-panel')
            else:
                response = request.POST.get('next', '/')
                return HttpResponseRedirect(response)
        else:
            return redirect('login')
        
        
def login_page(request):
    return render(request, 'login.html')