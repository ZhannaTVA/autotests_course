# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("args, expected", [
    ((225, 5), 45.0),
    ((121, -11, 5), -2.2),
    pytest.param((1.0, 0.0, 0.5), 'division by zero', marks=pytest.mark.smoke),
    ((), 'without params'),
    pytest.param((10.0, 2, 0.2), 25.0, marks=pytest.mark.skip(reason='bad test'))
])
def test_all_division(args, expected):
    match expected:
        case 'division by zero':
            with pytest.raises(ZeroDivisionError):
                all_division(*args)
        case 'without params':
            with pytest.raises(IndexError):
                all_division(*args)
        case _:
            assert all_division(*args) == expected