from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import ICohm

DATA_MAX = 9999999
EMPTY_SEARCH = [['Part Number', '', 'Ture', 0, 9999999, 0, 9999999, '', 0, 9999999, 0, 9999999, ''], [None, None, None, 0, 9999999, 0, 9999999, None, 0, 9999999, 0, 9999999, None]]


def SearchDataProcess(get_data, is_max=False):
    if get_data != '' and get_data is not None:
        get_data = int(get_data)
    elif is_max is True:
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
    producter = request.POST.get('producter')
    value_min = SearchDataProcess(request.POST.get('value_min'))
    value_max = SearchDataProcess(request.POST.get('value_max'), True)
    tol_min = SearchDataProcess(request.POST.get('tol_min'))
    tol_max = SearchDataProcess(request.POST.get('tol_max'), True)
    pack_type =request.POST.get('pack_type')

    search_data = [search_type, search_context, search_kind, voltage_min, voltage_max, height_min, height_max, producter, value_min, value_max, tol_min, tol_max, pack_type]
    if search_data in EMPTY_SEARCH:
        ohm_data = None
    elif search_type == 'Description':
        ohm_data = ICohm.objects.filter(Description__contains=search_context, VoltageRating__gte=voltage_min, VoltageRating__lte=voltage_max, Height_mm__gte=height_min, Height_mm__lte=height_max,
                                        OhmValue__gte=value_min, OhmValue__lte=value_max, Tolerance__gte=tol_min, Tolerance__lte=tol_max)
    else:
        ohm_data = ICohm.objects.filter(PartNumber__contains=search_context)

    return render(request, 'PdmSearchPage/SearchHompage.html', {'ohm_data': ohm_data, 'search_data': search_data})


def ShowDetail(request):
    # request.GET.get()
    return HttpResponse('页面正在开发')