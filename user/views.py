from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def user(request):
    return render(request,'user/user.html')
