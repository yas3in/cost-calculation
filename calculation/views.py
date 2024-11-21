from django.shortcuts import render
from calculation.models import Calculater
import jdatetime, datetime
from calculation.forms import GetDataForm


def index(request):
    return render(request, 'index.html')


def calculater(request):
    date = jdatetime.date.today()
    form = GetDataForm({'date': str(date), 'user': request.user})
    return render(request, 'calculater.html', {'form': form})
