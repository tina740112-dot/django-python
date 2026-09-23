class A:
    x = []
a1=A()
a2=A()
a1.x.append(1)
a2.x.append(2)
print(a1.x)  # Output: [1, 2]
print(a2.x)  # Output: [1, 2]
###################################
class B:
    def __init__(self):
        self.y = []#實例屬性，每個物件各自擁有
a3=B()
a4=B()
a3.y.append(1)
a4.y.append(2) 
print(a3.y)
print(a4.y)  # Output: [2]