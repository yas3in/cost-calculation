from django.shortcuts import render
from django.http import Http404
from calculation.models import Calculater
import jdatetime, datetime
from calculation.forms import GetDataForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'index.html')


@login_required
def calculater(request):
    date = jdatetime.date.today()
    form = GetDataForm({'date': str(date), 'user': request.user})
    response = {}
    response['cost'] = request.POST.get('cost', None)
    response['date'] = request.POST.get('date', None)
    response['description'] = request.POST.get('description', None)
    if form.is_valid():
        Calculater.objects.create(user=request.user, cost=response['cost'], description=response['description'], date=response['date'])
        return render(request, 'calculater.html', {'form': form})
    else:
        return Http404
