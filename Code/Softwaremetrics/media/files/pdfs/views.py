from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"sagar.html")
def register(request):
    s=request.POST.get("course")
    return render(request,"sagar.html", {"message" : s})
