#! /usr/bin/python
#coding=utf-8

class Father:
	def __init__(self):
		self.x = 50
	def printInfo(self):
		print(f"父類別方法:x={self.x}")

class Child(Father):
	def __init__(self):
		super().__init__()
		self.y = 100
	def printInfo(self):
		super(Child, self).printInfo()
		print(f"子類別方法 y={self.y}")

C = Child()
C.printInfo()
