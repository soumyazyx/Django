from django.shortcuts import render


def helloworldhome(request):
    return render(request, 'helloworld/hell.html')
