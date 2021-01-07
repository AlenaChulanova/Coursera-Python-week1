# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек
# нужно заплатить за N пирожков.
A = int(input())
B = int(input())
N = int(input())
costCoins = (A * 100 + B) * N
Rub = costCoins // 100
coins = costCoins % 100
print(Rub, coins)
