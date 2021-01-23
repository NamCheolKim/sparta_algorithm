# 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

input = "abcba"


def is_palindrome(string):

    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1])


print(is_palindrome(input))
