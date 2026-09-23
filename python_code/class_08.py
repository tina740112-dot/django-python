#! /usr/bin/python
#coding=utf-8

class Emp:
	def __init__(self):
		self.Salary = 0
	def set_salary(self,Salary):
		if (Salary>40000):
			self.Salary=40000
		else:
			self.Salary=Salary
	def ShowSal(self):
		print(str(self.Salary))

class Manager(Emp):
	def __init__(self):
		super().__init__() # 呼叫父類別的建構方法，不然Salary不會被初始化
		self.Bonus = 0
	def set_salary(self,Salary): #override
		if (Salary>60000):
			self.Salary=60000
		else:
			self.Salary=Salary

	def ShowSal(self): #override
		print(str(self.Salary+self.Bonus))

John=Emp()
John.set_salary(50000)
John.ShowSal()
John.Salary=100
John.ShowSal()

Mary=Manager()
Mary.set_salary(70000)
Mary.Bonus=20000
Mary.ShowSal()
