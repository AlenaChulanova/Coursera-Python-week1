# Напишите программу, которая по данному числу N от 1 до 9
# выводит на экран N пингвинов.
# Изображение одного пингвина имеет размер 5×9 символов,
# между двумя соседними пингвинами
# также имеется пустой (из пробелов) столбец.
N = int(input())
s1 = '   _~_    '
s2 = '  (o o)   '
s3 = ' /  V  \\  '
s4 = '/(  _  )\\ '
s5 = '  ^^ ^^   '
print(s1 * N)
print(s2 * N)
print(s3 * N)
print(s4 * N)
print(s5 * N)
