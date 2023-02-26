#Сложность Q(n)
# Пускаем число в цикл, пока оно не станет равно нулю
# Если число четное, то делим пополам
# Иначе отнимаем единицуgit commit -m
# В конце каждой операции увеличиваем счетчик
def numberOfSteps(num):
    steps = 0
    while num != 0:
        if num % 2 == 1:
            num -= 1
        else:
            num = num//2
        steps += 1

    return steps
print(numberOfSteps(7))