# Дано натуральное число. Найдите цифру,
# стоящую в разряде десятков в его десятичной записи
# (вторую справа цифру или 0, если число меньше 10).
N = int(input())
hundreds = N // 100
tens = N // 10 - hundreds * 10
print(tens)
