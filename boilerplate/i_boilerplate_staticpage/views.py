from django.shortcuts import render


def i_boilerplate_staticpage_home(request):
    return render(request, 'i_boilerplate_staticpage/home.html')
