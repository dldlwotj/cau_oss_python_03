# %%

"""
area_rectangle, area_right_triangle, area_ellipse �Լ��鿡��
���� �߻� �� 0������ ���� �Է��� �� �����ϴٸ� ����ϵ��� ����!
"""

import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("Please input positive number for width and height!")
# implement exception handler

myline.set_length(20, 30)
width, height = myline.get_length()
try:
    right_triangle = figure.area_right_triangle(width, height)
    print(right_triangle)
except ValueError:
    print("Please input positive number for width and height!")
# implement exception handler

myline.set_length(30, 40)
width, height = myline.get_length()
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("Please input positive number for width and height!")