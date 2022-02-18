class Shape:     
    def area(self, area = 0):
        return area 

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self, length):
        return length ** 2 

a = Square(Shape)
print(a.area(int(input())))

