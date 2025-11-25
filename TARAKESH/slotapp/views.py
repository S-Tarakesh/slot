from django.shortcuts import render
# Create your views here.
class timetable:
    def time(request):
        return render(request,"static\time.html")
