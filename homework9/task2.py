# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time

# Здесь пишем код
def func_log(file_log='log.txt', *args, **kwargs):
    """
    Декоратор пишет в файл имя и время вызова декорируемой функции
    """
    def decorator_for_fuc(func):
        def wrapped():
            with open(file_log, 'a+', encoding='utf-8') as log_file:
                log = f"{func.__name__} вызвана " \
                      f"{datetime.datetime.strftime(datetime.datetime.now(), '%d.%m %H:%M:%S')}\n"
                log_file.write(log)
            func(*args, **kwargs)

        for k in ('__name__', '__doc__'):
            value = getattr(func, k)
            setattr(wrapped, k, value)

        return wrapped

    return decorator_for_fuc


if __name__ == '__main__':
    @func_log()
    def func1():
        """sleep 1 sec"""
        time.sleep(1)


    @func_log(file_log='func2.txt')
    def func2():
        """sleep 2 sec"""
        time.sleep(2)


    def func3():
        """sleep 3 sec"""
        time.sleep(3)


    func1()
    func2()
    func1()
    """функция с декоратором"""
    print(help(func1))
    print('------')
    """функция без декоратора"""
    print(help(func3))