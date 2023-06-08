# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generate_random_name():

    """генерируем слово из латинских букв от 1 до 15 символов"""
    def random_word():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15)))

    while True:
        first_word, second_word = random_word(), random_word()
        yield f'{first_word} {second_word}'

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))