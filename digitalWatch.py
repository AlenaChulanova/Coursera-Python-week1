# Дано число N. С начала суток прошло N минут.
# Определите, сколько часов и минут будут
# показывать электронные часы в этот момент.
N = int(input())
days = N // 60 // 24
# print('days =', days)
hours = (N - days * 1440) // 60
# print('hours =', hours)
minutes = (N % 60)
# print('minutes =', minutes)
print(hours, minutes)
