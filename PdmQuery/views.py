from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import ICohm

DATA_MAX = 9999999


def SearchDataProcess(get_data, is_max=False):
    if get_data != '':
        get_data = int(get_data)
    elif is_max == True:
        get_data = DATA_MAX
    else:
        get_data = 0
    return get_data

def SearchHome(request):
    search_type = request.POST.get('search_type')
    search_context = request.POST.get('search_context')
    search_kind = request.POST.get('search_kind')
    voltage_min = SearchDataProcess(request.POST.get('voltage_min'))
    voltage_max = SearchDataProcess(request.POST.get('voltage_max'), True)
    height_min = SearchDataProcess(request.POST.get('height_min'))
    height_max = SearchDataProcess(request.POST.get('height_max'), True)
    producter = SearchDataProcess(request.POST.get('producter'))
    value_min = SearchDataProcess(request.POST.get('value_min'))
    value_max = SearchDataProcess(request.POST.get('value_max'), True)
    tol_min = SearchDataProcess(request.POST.get('tol_min'))
    tol_max = SearchDataProcess(request.POST.get('tol_max'), True)
    pack_type =SearchDataProcess(request.POST.get('pack_type'))

    if search_type == 'Description' and len(search_context) >= 2:
        ohm_data = ICohm.objects.filter(Description__contains=search_context)
    elif search_type == 'Part Number' and len(search_context) > 2:
        ohm_data = ICohm.objects.filter(PartNumber__contains=search_context)
    else:
        ohm_data = None

    search_data = search_type, search_context, search_kind, voltage_min, voltage_max, height_min, height_max, producter, value_min, value_max, tol_min, tol_max, pack_type
    return render(request, 'PdmSearchPage/SearchHompage.html', {'ohm_data': ohm_data, 'search_data': search_data})


def ShowDetail(request):
    # request.GET.get()
    return HttpResponse('页面正在开发')