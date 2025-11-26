from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
# 
def time_view(request,*args, **kwargs):
        return render(request,"time.html",context={})
