from django.shortcuts import render
from django.http import Http404, HttpResponse
from calculation.models import Calculater
import jdatetime, datetime
from calculation.forms import GetDataForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'index.html')


@login_required
def calculater(request):
    form = GetDataForm(request.POST)
    if form.is_valid():
        form.save(user=request.user)
        return render(request, 'calculater.html', {'form': form})
    else:
        return HttpResponse(form.errors)
    