# from django.db import models

# class Students(models.Model):
#     cID = models.AutoField(primary_key=True) # 設定 cID 為主鍵，並自動遞增
#     cName = models.CharField(max_length=20, blank=False) # 設定 cName 為字串欄位，最大長度為 20，且不可為空
#     cSex = models.CharField(max_length=1, blank=False, default='F') # 設定 cSex 為字串欄位，最大長度為 1，且不可為空，預設值為 'F'
#     cBirthday = models.DateField(blank=False) # 設定 cBirthday 為日期欄位，且不可為空
#     # cBirthday = models.DateField(auto_now_add=True) # 設定 cBirthday 為日期欄位，且不可為空，並自動設為當前日期
#     # cBirthday = models.DateField(auto_now=True) # 設定 cBirthday 為日期欄位，且不可為空，並自動更新為當前日期
#     cEmail = models.CharField(max_length=100, blank=False) # 設定 cEmail 為字串欄位，最大長度為 100，且不可為空
#     cPhone = models.CharField(max_length=50, blank=False) # 設定 cPhone 為字串欄位，最大長度為 20，且不可為空
#     cAddr = models.CharField(max_length=255, blank=False) # 設定 cAddr 為字串欄位，最大長度為 200，且不可為空
#     cHeight = models.IntegerField(blank=True) # 設定 cHeight 為整數欄位，且可為空
#     cWeight = models.IntegerField(blank=True) # 設定 cWeight 為整數欄位，且可為空

from django.db import models

# Create your models here.
class Student(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, blank=False)
    cSex =  models.CharField(max_length=1, blank=False, default='F')
    # cBirthday = models.DateField(auto_now_add=True, null=False)
    #這個參數的預設值也為False，設定為True時，會在model物件第一次被建立時，
    #將欄位的值設定為建立時的時間，以後修改物件時，欄位的值不會再更新。
    #cBirthday = models.DateField(auto_now=True, null=False)
    #這個參數的預設值為false，當設定為true時，能夠在儲存該欄位時，
    #將其值設為目前時間，並且每次修改model，都會自動更新
    cBirthday = models.DateField(null=True, blank=True)
    cEmail = models.CharField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)
    cHeight = models.IntegerField(blank=True, null=True) 
    cWeight = models.IntegerField(blank=True, null=True)

#一個學生有多個成績(one to many)(students to scorelist)
class Scorelist(models.Model):
    id = models.AutoField(primary_key=True)
    #外來鍵，Scorelist 表中的 cID 欄位會連到 Student 表的主鍵 cID，刪除學生時一起刪除資料
    cID = models.ForeignKey('Student', on_delete=models.CASCADE, null=True) 
    course = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(blank=False)
    
#一個學生有一個密碼與權限(one to one)(students to permissions)
class Permissions(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.OneToOneField('Student', on_delete=models.CASCADE, null=True)
    passwd = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=2, blank=False) #0管理者 #1一般使用者

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=32, blank=False)
    authors = models.ManyToManyField(to='Author')

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    aID = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=32, blank=False)
