from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse(u'Hello, World!', content_type="text/plain")
def home(request):
    return render(request, 'index.html')

def css(request):
    return render(request, 'static_handler.html')

