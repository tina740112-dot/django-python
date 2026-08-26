from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict

def test(request):
    # datas = Student.objects.all()  # 取得所有學生資料
    # # print(type(datas))  # 印出資料型態
    # for data in datas:
    #     # print(type(data)) # data 為 Student 物件
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    # datas = Student.objects.values('cID','cName','cEmail')
    # print(type(datas)) # QuerySet
    # for data in datas:
    #     # print(type(data)) # 'dict'
    #     print(data)
    ###############
    # datas = Student.objects.values("cSex").distinct()
    # print(type(datas)) # QuerySet
    # for data in datas:
    #     # print(type(data)) # 'dict'
    #     print(data)
    ###############
    # data = Student.objects.get(cID=3) # 取得單筆資料
    # # print(type(data)) # Student object
    # print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    # datas = Student.objects.filter(cSex='M')  # 取得符合條件的資料
    # # print(type(datas))  # QuerySet
    # for data in datas:
    #     # print(type(data))  # Student object
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    #　想要由 Student 資料表中找出座號大於 5 的男生
    # __gte # greater than or equal to, >=
    # __lte # less than or equal to, <=
    # datas = Student.objects.filter(cID__gt=5, cSex='M')  # 取得符合條件的資料
    # # __gt ==> >
    # # , ==> and

    # for data in datas:
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    # 資料表中找出座號等於 1 號或座號大於等於 9 號的人
    # from django.db.models import Q
    # # datas = Student.objects.filter(Q(cID__gt=5) & Q(cSex='M'))  # 取得符合條件的資料
    # datas = Student.objects.filter(Q(cID=1)|Q(cID__gte=9))  # 取得符合條件的資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出

    # 資料表中找出座號大於等於 4 且小於等於 6 的學生資料 
    # datas = Student.objects.filter(cID__range=[4, 6])  # 取得符合條件的資料
    # # datas = Student.objects.filter(cID__gte=4, cID__lte=6)  # 取得符合條件的資料

    # for data in datas:
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    # 資料表中找出座號為 1,3,5,9 的學生資料
    # datas = Student.objects.filter(cID__in=[1,3,5,9])  # 取得符合條件的資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    #　資料表中，出電話號碼是「0918」開頭的學生資料 
    # datas = Student.objects.filter(cPhone__startswith='0918')  # 取得符合條件的資料
    # 資料表中，找出學生的地址中有「建國」這個字的資料
    # datas = Student.objects.filter(cAddr__contains='建國')  # 取得符合條件的資料

    # for data in datas:
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    # datas = Student.objects.all().order_by('cBirthday')  # 取得所有學生資料，並依照 cID 欄位由小到大排序
    # datas = Student.objects.all().order_by('-cBirthday')  # 取得所有學生資料，並依照 cID 欄位由大到小排序
    # datas = Student.objects.all().order_by('cSex', '-cBirthday')  
    # # 取得所有學生資料，並依照 cSex 欄位由小到大排序，若 cSex 相同則依照 cBirthday 欄位由大到小排序

    # for data in datas:
    #     print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    ###############
    # datas = Student.objects.all()[:2]  # 取得前兩筆資料
    # datas = Student.objects.all()[0:2]  # 取得前兩筆資料，顯示引索 0~1 的資料，索引 2 的資料不會顯示
    #datas = Student.objects.all()[4:6]  # 取得第 5 筆到第 6 筆資料，顯示引索 4~5 的資料，索引 6 的資料不會顯示
    #for data in datas:
    #    print(model_to_dict(data))  # 將資料轉換為字典格式並印出
    from django.db.models import Avg, Max, Min, Sum, Count
    #datas = Scorelist.objects.aggregate(Sum('score'))
    #print(datas)#將資料轉換為字典格式並印出
    #####################
    datas=Scorelist.objects.filter(course='國文').aggregate(Avg('score'))
    print(datas)
    #####################
    #datas=Student.objects.aggregate(Count('cID'))
    #print(datas)
    #datas=Scorelist.objects.filter(course='國文').aggregate(Max('score'))
    #print(datas)
    #####################
    #datas=Scorelist.objects.values_list('cID').annotate(Sum('score'))
    #print(datas)
    #for data in datas:
    #    print(data)#格式為tuple
    #######################
    #datas=Scorelist.objects.values_list('cID').annotate(Avg('score'))
    #for data in datas:
    #    print(data)#格式為tuple
    
  #########################
#datas=Scorelist.objects.filter(cID__lte=5).values_list('cID').annotate(Sum('score'))
#說明:這段程式碼會先篩出cid小於等於5的資料，然後依照cid的分組，並計算每個cid的score總和，最後回傳一個queryset，裡面包含每個cid的score總和，並以tuple的形式呈現，每個tuple的第一個元素是cid，第二個元素是score總和。
#for data in datas:
#    print(data)#格式為tuple
#####################
#add data
#第一種方式:先建立物件，再呼叫save()方法
#student_exists = Student.objects.filter(cName='Bill3').exists()
#if not student_exists:
#    add=Student(cName='Bill3',cSex='M',cBirthday='2000-01-01',cEmail='bill3@example.com',cPhone='0912345678',cAddr='台北市中正區建國南路一段1號',cHeight=180,cWeight=70)
#    add.save()
#    print('Add data successfully')
#else:
#  print('Data already exists')
#二種方法:直接使用create()方法建立覺件並儲存
#student_exists=Student.objects.filter(cName='Bill4').exists()
##if not student_exists:
##    Student.objects.create(cName='Bill4',
##                           cSex='M',
##                           cBirthday='2000-01-01',
##                           cEmail='bill4@example.com',
##                           cPhone='0912345678',
##                           cAddr='台北 市中正區建國南路一段1號',
##                           cHeight=180,
##                           cWeight=70)
##    print('Add data successfully')
##else:
##    print('Data already exists')
    
#UPDATE DATA
#用於單筆資料更新，先使用get()方法取得要更新的資料，然後修改欄位值，最後呼叫save()方法儲存更新後的資料。

##try:
##    update = Student.objects.get(cID=11)
##    update.cHeight = 190
##    update.cWeight = 80
##    update.save()
##    print('Update data successfully')
##except:
##    print('Student not found')

##########################
#用於多筆資料的更新，使用filter()方法取得要更新的資料，再使用update()方法修改欄位值
#try:
#    update_count = Student.objects.filter(cID=4).update(cAddr='台北市中正區建國南路一段1號',cPhone='09265874')
#    print(f'{update_count} 筆資料');
#except:
#    print('Update failed')
#################################
#delete data
student_exists = Student.objects.filter(cID__gte=13).exists()
if student_exists:
    delete_count = Student.objects.filter(cID__gte=13).delete()
    print(f'{delete_count[0]} 筆資料已刪除')
else:
    print('No data to delete')
    
#return HttpResponse("Hello, world. You're at the test page.")