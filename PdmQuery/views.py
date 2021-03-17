from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ICohm


def SearchHome(request):
    ohm_data = ICohm.objects.filter(OhmValue__range=[200, 1100]).filter(OhmValue__range=[500, 1100])
    return render(request, 'PdmSearchPage/SearchHompage.html', {'ohm_data': ohm_data})


def ShowDetail(request):
    # request.GET.get()
    return HttpResponse('页面正在开发')