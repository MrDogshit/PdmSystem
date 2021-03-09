from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ICohm


def Search_home(request):
    ohm_data = ICohm.objects.all()
    return render(request, 'PdmSearchPage/SearchHompage.html', {'ohm_data': ohm_data})