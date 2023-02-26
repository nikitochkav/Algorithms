#Сложность Q(n)
# Пускаем число в цикл пока оно не станет равно нулю
# Если число четное, то делим пополам
# Иначе отнимаем единицу
# В конце каждой операции увеличиваем счетчик
def numberOfMatches(n: int) -> int:
    matches = 0
    while n > 1:
        if n % 2 == 1:
            matches += (n - 1) // 2
            n = 1 + (n - 1) // 2
        else:
            matches += n // 2
            n = n // 2
    return matches

print(numberOfMatches(n = 65))