from django.shortcuts import render
# Create your views here.
# 
def time_view(request,*args, **kwargs):
        return render(request,"time.html",context={})
