# 피보나치 수열의 100번째 수를 구하시오.

input = 100
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    n_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)

    fibo_memo[n] = n_fibo

    return n_fibo


print(fibo_dynamic_programming(input, memo))
