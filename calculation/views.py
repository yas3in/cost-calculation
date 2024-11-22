from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from calculation.models import Calculater
from calculation.forms import GetDataForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import pandas as pd
import jdatetime


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
    user = Calculater.objects.all().values()
    data = pd.DataFrame(user)
    print(data['description'])