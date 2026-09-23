class SmallMath:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
      
    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "none"

s = SmallMath(10, 5)
print(s.add())       # Output: 15
print(s.subtract())  # Output: 5
print(s.multiply())  # Output: 50
print(s.divide())    # Output: 2.0
