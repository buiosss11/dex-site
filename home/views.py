from django.shortcuts import render
from datetime import datetime
# base_path = 'home/'
# Create your views here.
#이슬 성공
def index(request):

    return render(request,'home/base.html')
