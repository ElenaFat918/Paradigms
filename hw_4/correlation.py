def mult_el(ar_1, ar_2):
    result = []
    lst = zip(ar_1, ar_2)
    for val in lst:
        result.append(val[0] * val[1])
    return result


def diff_avg(arr):
    res = []
    avg = sum(arr) / len(arr)
    for el in arr:
        res.append(el - avg)
    return res


def square_el(arr):
    lst = []
    for el in arr:
        lst.append(el ** 2)
    return lst


def correlation(arr_1, arr_2):
    core = sum(mult_el(diff_avg(arr_1), diff_avg(arr_2))) / (
                (sum(square_el(diff_avg(arr_1))) * sum(square_el(diff_avg(arr_2)))) ** 0.5)
    return core


array_first = [14, 25, 12, 27, 19]
array_second = [22, 10, 24, 10, 7]

print(correlation(array_first, array_second))
