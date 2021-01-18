input = [7, 3, 1, 9, 6, 8, 5]


def find_max_num(array):

    max_num = array[0]

    for num in array:
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)
