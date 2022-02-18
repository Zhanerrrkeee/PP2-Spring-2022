import math

class Point:
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def show (self):
        print(f'{self.x1} {self.y1}')
        print(f'{self.x2} {self.y2}')
              
    def move (self,x_1,x_2,y_1,y_2):
        self.x1 = x_1
        self.x2 = x_2
        self.y1 = y_1
        self.y2 = y_2

    def dist (self):
        return math.sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2))

a = Point(int(input("Enter x1")),int(input("Enter x2")),int(input("Enter y1")),int(input("Enter y2")))
r = "{:.5f}"

print(f'If you want to show coordinates type "1"')
print(f'If you want change coordinates type "2"')
print(f'If you want to know the distance between two points type "3"')
enter = int(input())
if enter == 1:
    a.show()
    print(f'If you want change coordinates type "2"')
    print(f'If you want to know the distance between two points type "3"')
    enter = int(input())
if enter == 2:
    a.move(int(input("Enter x1")),int(input("Enter x2")),int(input("Enter y1")),int(input("Enter y2")))
    print(f'If you want to show coordinates type "1"') 
    print(f'If you want to know the distance between two points type "3"')
    enter = int(input())
if enter == 3 :
    print(r.format(a.dist()))
    print(f'If you want change coordinates type "2"')
    print(f'If you want to know the distance between two points type "3"')
    enter = int(input())


