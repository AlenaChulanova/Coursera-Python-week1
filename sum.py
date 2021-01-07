# Дано трехзначное число. Найдите сумму его цифр.
N = int(input())
hundreds = N // 100
tens = N // 10 - hundreds * 10
# print(hundreds + tens + N % 10)
# print(hundreds)
# print(tens)
print(hundreds + tens + N % 10)
