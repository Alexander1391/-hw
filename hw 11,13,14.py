import math

print('задача 11')
def degrees2radians(degrees):
    i = (degrees * math.pi) / 180
    return i
res1 = degrees2radians (math.cos(60))
res2 = degrees2radians (math.cos(45))
res3 = degrees2radians (math.cos(40))
print(float(res1), float(res2), float(res3))


print('задача 13')
def triangle_square_and_perimeter(a, b):
    perimeter = a + b + (math.sqrt(a ** 2 + b ** 2))
    square = a * b / 2
    return perimeter, square
result1, result2 = triangle_square_and_perimeter(4, 7)
print(result1, result2)

print('задача 14')
def is_even(number):
    return number % 2 == 0
i = 2
if is_even(i):
    print('True')
else:
    print('False')

