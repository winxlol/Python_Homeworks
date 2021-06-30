import math


def closest_point_to_center(num1, num2, num3, num4):
    x1 = abs(num1)
    y1 = abs(num2)
    x2 = abs(num3)
    y2 = abs(num4)

    if (
            x1 <= x2 and y1 < y2 or
            x1 < x2 and y1 <= y2 or
            x1 == x2 and y1 == y2
    ):
        num1 = math.floor(num1)
        num2 = math.floor(num2)
        print(f"({num1}, {num2})")
    else:
        num3 = math.floor(num3)
        num4 = math.floor(num4)
        print(f"({num3}, {num4})")


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

closest_point_to_center(num1, num2, num3, num4)
