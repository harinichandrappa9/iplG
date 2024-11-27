from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captaindhoni(request):
    return HttpResponse('<h1>THALA MSD</h1><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQA4-fxXm-gUeqcc3idXuKp4DW4Rj98m7AmiKZiRB7VCGn_73Vcn1qfe5ZoH0TPC3lmuIbBS48_McJH6S5qzQ_s0w">')
