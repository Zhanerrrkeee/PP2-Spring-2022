from operator import length_hint


class Shape:
    def area(self, area = 0):
        return area 

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self, length):
        return length ** 2 



class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

a = Rectangle(int(input()),int(input()))
print(a.area())        
            