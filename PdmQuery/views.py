from django.shortcuts import render
from django.shortcuts import HttpResponse


def Search_home(request):
    return render(request, 'PdmSearchPage/SearchHompage.html')