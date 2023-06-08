# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_positive_number():
    assert all_division(35, 7) == 5.0

def test_negative_number():
    assert all_division(12, -3, 2) == -2.0

@pytest.mark.smoke
def test_without_args():
    with pytest.raises(IndexError):
        all_division()

def test_many_args():
    assert all_division(96, 68, 30, 25, 18, 3, 0.5) == 6.971677559912855e-05

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(100, 0)