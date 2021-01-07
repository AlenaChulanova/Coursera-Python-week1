# Напишите программу, которая считывает целое число
# и выводит текст, аналогичный приведенному в примере
# The next number for the number 179 is 180.
# The previous number for the number 179 is 178.
N = int(input())
print('The next number for the number ', N, ' is ', N + 1, '.', sep='')
print('The previous number for the number ', N, ' is ', N - 1, '.', sep='')
