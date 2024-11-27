from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return HttpResponse('<h1>ROHIT SHARMA</h1><img src="https://imagesvs.oneindia.com/webp/img/2024/11/mumbaiindians5-1732472253.jpg">')
