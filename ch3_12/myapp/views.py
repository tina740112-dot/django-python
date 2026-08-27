from urllib import request

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

def index(request):
  #orm語法
    resultlist=Students.objects.all()
    #for data in resultlist:
    #    print(model_to_dict(data))#將資料轉為字典格式並印出
    data_count=resultlist.count()#計算資料筆數
    print(data_count)
    #return HttpResponse("hello")
    return render(request,'index.html',locals())#將所有本地變數傳給index.html
from django.shortcuts import redirect
def post(request):
    if request.method == 'POST':
        cname=request.POST.get('cname')#取得使用者輸入的姓名
        csex=request.POST.get('csex')#取得使用者輸入的性別
        cbirthday=request.POST.get('cbirthday')#取得使用者輸入的生日
        cemail=request.POST.get('cemail')#取得使用者輸入的電子郵件
        cphone=request.POST.get('cphone')#取得使用者輸入的電話
        caddr=request.POST.get('caddr')#取得使用者輸入的地址
        print(f'cname:{cname}, csex: {csex}, cbirthday: {cbirthday}, cemail: {cemail},cphone: {cphone}, caddr: {caddr}')#印出使用者輸入的資料
        add=Students(cname=cname,csex=csex,cbirthday=cbirthday,cemail=cemail,cphone=cphone,caddr=caddr)#建立學生物件
        add.save()#儲存學生物件
        return redirect('index')#重新導向到index頁面
       
        return HttpResponse("資料已送出")#回傳資料已送出
    else:
        return render(request,'post.html',locals())#將所有本地變數傳給post.html
      
def edit(request, id):
    if request.method == 'POST':
        cname=request.POST.get('cname')#取得使用者輸入的姓名
        csex=request.POST.get('csex')#取得使用者輸入的性別
        cbirthday=request.POST.get('cbirthday')#取得使用者輸入的生日
        cemail=request.POST.get('cemail')#取得使用者輸入的電子郵件
        cphone=request.POST.get('cphone')#取得使用者輸入的電話
        caddr=request.POST.get('caddr')#取得使用者輸入的地址
        print(f'id:{id}')#印出使用者輸入的資料
        print(f'cname:{cname}, csex: {csex}, cbirthday: {cbirthday}, cemail: {cemail},cphone: {cphone}, caddr: {caddr}')#印出使用者輸入的資料
        update=Students.objects.get(cid=id)#取得學生物件
        update.cname=cname#修改學生物件的姓名
        update.csex=csex#修改學生物件的性別
        update.cbirthday=cbirthday#修改學生物件的生日
        update.cemail=cemail#修改學生物件的電子郵件
        update.cphone=cphone#修改學生物件的電話
        update.caddr=caddr#修改學生物件的地址
        update.save()#儲存學生物件
        
       
        return redirect('index')#重新導向到index頁面
    else:
        obj_data=Students.objects.get(cid=id)
        print(model_to_dict(obj_data))#將資料轉為字典格式並印出
        return render(request,'edit.html',locals())#將所有本地變數傳給edit.html
  
def delete(request, id):
    if request.method == 'POST':
        delete_data = Students.objects.get(cid=id)#取得學生物件
        delete_data.delete()#刪除學生物件
        return redirect('index')#重新導向到index頁面
    else: 
        obj_data=Students.objects.get(cid=id)
        print(model_to_dict(obj_data))#將資料轉為字典格式並印出
        #return HttpResponse(f"HELLO DELETE {id}")
        return render(request,'delete.html',locals())#將所有本地變數傳給delete.html

  