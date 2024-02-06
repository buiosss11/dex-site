from django.shortcuts import render
from datetime import datetime
# base_path = 'home/'
# Create your views here.
def index(request):

    return render(request,'home/base.html')
