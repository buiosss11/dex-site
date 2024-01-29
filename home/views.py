from django.shortcuts import render
from datetime import datetime
base_path = 'home/'
# Create your views here.
def index(request):
    year  = datetime.today().year
    month  = datetime.today().month
    day  = datetime.today().day
    context = {
        "year": year,
        "month": month,
        "day": day,
    }
    print(year)
    return render(request,'home/index.html',context)

def items(request,item):
    if item == 'news':
        templates_path = base_path+'news.html'
    elif item == 'dex':
        templates_path = base_path+'dex.html'
    elif item == 'rpa_docs':
        templates_path = base_path+'rpa.html'
    elif item == 'apps_docs':
        templates_path = base_path+'apps.html'
    elif item == 'bi_docs':
        templates_path = base_path+'bi.html'
    elif item == 'create_account':
        templates_path = base_path+'create_account.html'
        
    
    return render(request,templates_path)