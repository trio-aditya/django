from django.http import HttpResponse
from django.shortcuts import render

"""
#method views index
#django.http import HttpResponse
def index(request):
    return HttpResponse("Ini adalah halaman index")
"""

#method views index
#django.shortcuts import render
def index(request):
    return render(request,'index.html')

#method about
def about(request):
    return render(request,'about.html')