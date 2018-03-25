import math

def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
       x_1 = ((-1 * b) + math.sqrt(discriminant)) / (2 * a)
       x_2 = ((-1 * b) - math.sqrt(discriminant)) / (2 * a)
       return x_1, x_2
    elif discriminant == 0:
       x_1 = ((-1 * b) / (2 * a))
       x_2 = None
       return x_1,x_2
    else:
       return (None, None)

x_1, x_2 = solve_quadratic_equation(7, 34, 5)
print(x_1, x_2)


def circle_coordinates(x, y, r):
    xmin = x - r;
    xmax = x + r;
    ymin = y - r
    ymax = y + r

    return xmin, xmax, ymin, ymax

def circles_intersect(x1, y1, r1, x2, y2, r2):
    circle1 = circle_coordinates(x1, y1, r1)
    circle2 = circle_coordinates(x2, y2, r2)

    resX = circle1[0] <= circle2[0] and circle1[1] >= circle2[0]
    resY = circle1[2] <= circle2[2] and circle1[3] >= circle2[2]

    return resX or resY

print(circles_intersect(2, 4, 0, 3, 6, 0))

