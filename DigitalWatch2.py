# С начала суток прошло N секунд. Выведите, что покажут часы.
# в формате h:mm:ss, то есть сначала записывается
# количество часов (число от 0 до 23),
# потом обязательно двузначное количество минут,
# затем обязательно двузначное количество секунд.
N = int(input())
days = N // 86400
print('days =', days)
hours = (N // 60 - days * 1440 * 60 * 24) // 60
print('hours =', hours)
minutes = (N // 3600 - hours) // 60
print('minutes =', minutes)
seconds = (N % 60)
print('seconds =', seconds)
print(hours, minutes, seconds)

