input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for i in range(2, number + 1):
        for j in prime_list:
            if i % j  == 0 and j * j <= i:
                break
        else:
            prime_list.append(i)

    return prime_list

result = find_prime_list_under_number(input)
print(result)
