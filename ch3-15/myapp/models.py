from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cBirthday = models.DateField(null=True, blank=True, verbose_name="生日")
    tel = models.CharField(max_length=16, null=True, blank=True, verbose_name="電話")
    # verbose_name="生日"：在 Django 管理介面中顯示的欄位名稱是「生日」（中文顯示更友善）。


    def __str__(self):
        return self.username
    #是 Python 類別中的特殊方法 __str__，用來定義當物件被轉換成字串時要顯示什麼內容。這在 Django 中特別重要，因為它會影響下列情況的顯示方式： 