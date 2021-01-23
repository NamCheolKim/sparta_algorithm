# 60에서 0까지 숫자를 출력하시오.

def count_down(number):
    if number < 1:
        return
    print(number)
    count_down(number - 1)


count_down(60)
