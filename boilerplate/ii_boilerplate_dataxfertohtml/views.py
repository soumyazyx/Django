from django.shortcuts import render


def ii_boilerplate_dataxfertohtml_home(request):
    dummy = {
        'name': 'soumya',
        'age': 99
    }
    context = {'data': dummy}
    return render(request, 'ii_boilerplate_dataxfertohtml/home.html', context)
