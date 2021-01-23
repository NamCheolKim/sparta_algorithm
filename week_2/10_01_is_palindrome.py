# 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

input = "abcba"


def is_palindrome(string):

    n = len(string)

    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False
    return True


print(is_palindrome(input))


# strs = []
# for char in string:
#     if char.isalnum():
#         strs.append(char)
#
# while len(strs) > 1:
#     if strs.pop(0) != strs.pop():
#         return False
