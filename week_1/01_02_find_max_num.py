# 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

input = [7, 3, 1, 9, 6, 8, 5]


def find_max_num(array):

    max_num = array[0]

    for num in array:
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)
