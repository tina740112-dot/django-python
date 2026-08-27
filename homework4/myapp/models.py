from django.db import models

class temperature_db(models.Model):
    myid = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField()
    temperature =  models.FloatField()
    # cBirthday = models.DateField(auto_now_add=True, null=False)
    #這個參數的預設值也為False，設定為True時，會在model物件第一次被建立時，
    #將欄位的值設定為建立時的時間，以後修改物件時，欄位的值不會再更新。
    #cBirthday = models.DateField(auto_now=True, null=False)
    #這個參數的預設值為false，當設定為true時，能夠在儲存該欄位時，
    #將其值設為目前時間，並且每次修改model，都會自動更新
    humidity = models.FloatField()
    timestamp = models.DateTimeField()
    #cphone = models.CharField(max_length=50, blank=False)
    #caddr = models.CharField(max_length=255, blank=False)


# Create your models here.
