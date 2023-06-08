# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def summa(a, b):
    """
    складывает значения a и b
    """
    return a + b


class Test:

    def test_number(self):
        assert summa(4, 2) == 6

    def test_str(self, execution_time):
        assert summa('spider-', 'man') == 'spider-man'

    def test_type_error(self):
        with pytest.raises(TypeError):
            summa('4', 2)