""" Задача №1 Дан список целых чисел numbers.
Необходимо написать в императивном стиле процедуру
для сортировки числа в списке в порядке убывания.
Можно использовать любой алгоритм сортировки"""


# Императивный метод: метод сортировки "вручную", прямое взаимодествие с элементами списка
def sort_list(numbers):
    for j in range(len(numbers)-1):
        for i in range(len(numbers)-1-j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


# Декларативный метод: метод сортировки через встроенную функцию
def sort_list_2(numbers):
    numbers.sort()


# Косвенная часть программы
if __name__ == "__main__":
    lst = [6, 3, 9, 7, 5, 1]
    sort_list(lst)
    print(*lst)
    lst_2 = [6, 3, 9, 7, 5, 1]
    sort_list_2(lst_2)
    print(*lst_2)
