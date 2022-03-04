import math
num_side = int(input())
length_side = int(input())
apothema = length_side / (2 * math.tan ( math.pi / num_side))
area = (num_side * length_side * apothema) /2
print(int(area))