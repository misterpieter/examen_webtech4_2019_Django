from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render

# 29 March 2019 at 11 pm UK time. + 1h to compensate UK time
# Create your views here.
def index(request):

    Today = datetime.datetime.now()
    brexit = datetime.datetime(2019, 3, 29,23,0,0)

    remaining = brexit - Today

    return HttpResponse("Time remaining untill BREXIT: {0}ms".format(remaining))