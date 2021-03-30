from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import ICohm


def SearchDataProcess(**kwargs):
    for key, value in kwargs.items():
        if kwargs[key] is None:
            del kwargs[key]
    return kwargs


def SearchHome(request):
    search_type = request.POST.get('search_type')
    search_context = request.POST.get('search_context')
    search_kind = request.POST.get('search_context')
    voltage_min = request.POST.get('voltage_min')
    voltage_max = request.POST.get('voltage_max')
    height_min = request.POST.get('height_min')
    height_max = request.POST.get('height_max')
    producter = request.POST.get('producter')
    value_min = request.POST.get('value_min')
    value_max = request.POST.get('value_max')
    tol_min = request.POST.get('tol_min')
    tol_max = request.POST.get('tol_max')
    pack_type = request.POST.get('pack_type')

    ohm_data = ICohm.objects.filter(OhmValue__range=[200, 1100], PartNumber__gt=10010007)
    return render(request, 'PdmSearchPage/SearchHompage.html', {'ohm_data': ohm_data})


def ShowDetail(request):
    # request.GET.get()
    return HttpResponse('页面正在开发')