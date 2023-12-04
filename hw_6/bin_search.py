def bin_search(find_num, array):
    if find_num == array[0]:
        return 0
    if find_num == array[-1]:
        return len(array) - 1
    index_min = 0
    index_max = len(array) - 1
    while index_max - index_min > 1:
        ind = index_min + (index_max - index_min)//2
        if find_num == array[ind]:
            return ind
        elif find_num > array[ind]:
            index_min = ind
        else:
            index_max = ind
    return None


if __name__ == '__main__':
    lst = [1, 2, 5, 6, 7, 10, 13, 15, 16, 17, 19, 20]
    num = int(input('chislo: '))
    print(lst)
    print(f'index - {bin_search(num, lst)}')