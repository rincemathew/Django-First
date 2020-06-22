from django.shortcuts import render
from .models import AccessRecord,Topic,Webpage

def hello(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dic = {'insert':webpages_list }
    return render(request,'index.html',context=my_dic)
