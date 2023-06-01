"""
figure ����� �׸��� ���õ� �Լ� �� Ŭ������ �����ϴ� ����Դϴ�.
'line' Ŭ������ �̿��Ͽ� ���� ���̸� �����ϰų� �����ϴ� �۾��� �����ϸ�
'area_rectangle', 'area_ellipse', area_right_triangle' �Լ���
���� ���簢��, Ÿ��, �����ﰢ���� ���̸� ��ȯ�մϴ�.
"""

import math

class line:
    """
    'line' Ŭ������ ���� ���̿� ���� �����ϴ� Ŭ�����Դϴ�.
    �����δ� �ܺο��� ������ �� ���� '__width', '__height'�� ������,
    �ش� ������ �����ϰ� �����ϱ� ����
    'set_length'�� 'get_length' �޼ҵ带 �����մϴ�.
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """Ŭ������ ������ �� ó�� ���ο� ������ ���̸� �Է¹޽��ϴ�.
        Args:
            width (int or float): �ʱ� ���� ���� ����
            height (int or float): �ʱ� ���� ���� ����
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """���� ���̸� �����մϴ�.
        Args:
            width (int or float): �����ϰ��� �ϴ� ���� ����
            height (int or float): �����ϰ��� �ϴ� ���� ����
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """��ü�� ����� ���� ���̸� ��ȯ�մϴ�.
        Returns:
            int or float: ����� ���� ����
        """
        return self.__width, self.__height
    

def area_rectangle(width, height):
    """���̸� �Է¹޾� ���簢���� ���̸� ���ϴ� �Լ�
    Args:
        width (int or float): �غ��� ����
        height (int or float): ����
    Returns:
        int or float: ���簢���� ���̸� ��ȯ
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height

def area_ellipse(width, height):
    """���̸� �Է¹޾� Ÿ���� ���̸� ���ϴ� �Լ�
    Args:
        width (int or float): ª�� �������� ����
        height (int or float): �� �������� ����
    Returns:
        int or float: Ÿ���� ���̸� ��ȯ
    """
    if width <= 0 or height <= 0: raise ValueError
    return math.pi * width * height

def area_right_triangle(width, height):
    """���̸� �Է¹޾� �����ﰢ���� ���̸� ���ϴ� �Լ�
    Args:
        width (int or float): �غ��� ����
        height (int or float): ����
    Returns:
        int or float: �����ﰢ���� ���̸� ��ȯ
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2