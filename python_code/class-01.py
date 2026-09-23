# class:紅豆餅模板、藍圖、設計圖、無實體
# object:紅豆餅、房子、有實體

# 定義一個類別名為 MyClass、包含屬性(變數(int, float,list,str))和method(方法)/function(函式)
# 屬性，名詞、容器
# 方法，動詞、行為、功能
class MyClass:
    def __init__(self): #初始化方法
        self.text = "ABC" # 字串屬性
    def clear(self): # 方法
        self.text = "" # 清空字串屬性

################################
obj1 = MyClass() # 建立物件
# 取值
print(f"text={obj1.text}") #取值  #obj1=>text
# 改值
obj1.text = "DEF"
print(f"text={obj1.text}")
# 使用方法
obj1.clear() #呼叫方法
print(f"text={obj1.text}")
################################
class student:
    def __init__(self):
        self.sno =''#屬性，學號
        self.sname=''#屬性，姓名
    def iam(self):#方法，介紹自己
        print(f"my student number is {self.sno}, my name is {self.sname}")

s1=student()#建立物件
s1.sno='a0001'#設定學號
s1.sname='john'#設定姓名
s1.iam()#呼叫方法

s2=student()#建立物件
s2.sno='a0002'#設定學號 
s2.sname='mary'#設定姓名
s2.iam()#呼叫方法