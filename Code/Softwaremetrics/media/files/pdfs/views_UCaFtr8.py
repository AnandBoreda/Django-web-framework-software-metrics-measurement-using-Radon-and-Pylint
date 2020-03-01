from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# Create your views here.

# def base(request):
#     return render(request, 'base.html')

class HomePageView(ListView):
    model = Post
    template_name = 'base.html'