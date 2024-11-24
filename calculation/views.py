from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from calculation.models import Calculater
from calculation.forms import GetDataForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import pandas as pd
import jdatetime
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


@login_required
def insert_data(request):
    form = GetDataForm({'date': jdatetime.date.today(), 'user': request.user})
    if form.is_valid() is not None:
        form.save()
        print(request.POST)
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
    
       
def show_data(request):
    # user = User.objects.filter(user=request.user)
    dt = Calculater.objects.filter(user=request.user).values().order_by('-date', '-id')[:5]
    data = pd.DataFrame(dt)
    data = data.rename(columns={
        "cost": "هزینه",
        "date": "تاریخ",
        "description": "توضیح خرید"
    })
    data['هزینه'] = data['هزینه'].apply(lambda x: f"{x:,.0f} تومان")
    return render(request, 'show_data.html', 
                    {
                        'data': data.to_html(
                            columns=['هزینه', 'تاریخ', "توضیح خرید"], 
                            col_space=5, index=False,
                            justify='center', border=None
                        )
                    }
                )