from django.db import models
from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Date,Time=None
obj={
    datetime.today(),
    datetime.now()
}
def index(request):
    return HttpResponse("polls page")