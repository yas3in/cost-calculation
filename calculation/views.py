from django.shortcuts import render
from django.http import Http404, HttpResponse
from calculation.models import Calculater
from calculation.forms import GetDataForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import pandas as pd
import jdatetime


def index(request):
    return render(request, 'index.html')


@login_required
def calculater(request):
    form = GetDataForm(request.POST, {'date': jdatetime.date.today()})
    if form.is_valid() is not None:
        form.save(user=request.user)
        return render(request, 'calculater.html', {'form': form})
    else:
        return HttpResponse(form.errors)
    
    
def show_data(request):
    user = Calculater.objects.all()
    data = pd.DataFrame(
        {
            'users': user.user,
            'cost': user.cost
         }
    )
    return HttpResponse(data)