# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file1:
    costs, all_costs = 0, []
    for line in file1:
        if line.strip() != r'':
            costs += int(line)
        else:
            all_costs.append(costs)
            costs = 0
    all_costs.sort(reverse=True)
    three_most_expensive_purchases = sum(all_costs[:3])
# Здесь пишем код

assert three_most_expensive_purchases == 202346