"""
figure ����� �׸��� ���õ� �Լ� �� Ŭ������ �����ϴ� ����Դϴ�.
'line' Ŭ������ �̿��Ͽ� ���� ���̸� �����ϰų� �����ϴ� �۾��� �����ϸ�
'area_square', 'area_circle', area_regular_triangle' �Լ���
���� ���簢��, ��, ���ﰢ���� ���̸� ��ȯ�մϴ�.
"""

import math

class line:
    """
    'line' Ŭ������ ���� ���̿� ���� �����ϴ� Ŭ�����Դϴ�.
    �����δ� �ܺο��� ������ �� ���� '__length'�� ������,
    �ش� ������ �����ϰ� �����ϱ� ����
    'set_length'�� 'get_length' �޼ҵ带 �����մϴ�.
    """
    __length = 0

    def __init__(self, length):
        """Ŭ������ ������ �� ó�� ���� ���̸� �Է¹޽��ϴ�.
        Args:
            length (int or float): �ʱ� ���� �����Դϴ�.
        """
        self.__length = length

    def set_length(self, length):
        """���� ���̸� �����մϴ�.
        Args:
            length (int or float): �����ϰ��� �ϴ� ���� �����Դϴ�.
        """
        self.__length = length

    def get_length(self):
        """��ü�� ����� ���� ���̸� ��ȯ�մϴ�.
        Returns:
            int or float: ����� ���� �����Դϴ�.
        """
        return self.__length
    

def area_square(length):
    """���簢���� �� ���� ���̸� �Է¹޾� ���簢���� ���̸� ���ϴ� �Լ��Դϴ�.
    Args:
        length (int or float): ���簢���� �� ���� �����Դϴ�.
    Returns:
        int or float: ���簢���� ���̸� ��ȯ�մϴ�.
    """
    return length**2

def area_circle(length):
    """���� �������� ���̸� �Է¹޾� ���� ���̸� ���ϴ� �Լ��Դϴ�.
    Args:
        length (int or float): �������� �����Դϴ�.
    Returns:
        int or float: ���� ���̸� ��ȯ�մϴ�.
    """
    return math.pi * (length**2)

def area_regular_triangle(length):
    """���ﰢ���� �� ���� ���̸� �Է¹޾� ���ﰢ���� ���̸� ���ϴ� �Լ��Դϴ�.
    Args:
        length (int or float): ���ﰢ���� �� ���� �����Դϴ�.
    Returns:
        int or float: ���ﰢ���� ���̸� ��ȯ�մϴ�.
    """
    return math.sqrt(3) * (length**2) / 4