from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict


def search_list(request):
   if'cname'in request.GET:
      cname=request.GET['cname']#取得使用者輸入的姓名
      print(f'Received cname: {cname}')#印出使用者輸入的姓名
      datas=Students.objects.filter(cname__icontains=cname).order_by('-cid')#取得學生資料
   else:
      datas=Students.objects.all().order_by('-cid')#取得學生資料
     
    
    #for data in data:
    #    print(type(data))#data為student物件
    #    print(model_to_dict(data))#將資料轉為字典格式並印出
        
   # return HttpResponse("hello")
    #return render(request,'search_list.html',{'datas':datas})#將資料傳給search_list.html
   # return render(request,'search_list.html',locals())#將所有本地變數傳給search_list.html
  
   if not datas:
        errormessage="查無資料"
        #return render(request,'search_list.html',{'errormessage':errormessage})#將錯誤訊息傳給search_list.html
   return render(request,'search_list.html',locals())#將所有本地變數傳給search_list.html
# Create your views here.


def search_name(request):
 # return HttpResponse("hello")
  return render(request,'search_name.html',locals())#將所有本地變數傳給search_name.html