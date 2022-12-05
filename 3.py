#Сложность Q(n^2)
#Перебираем элементы из списка G
#Перебираем каждый элемент из списка S
#Если элементы одинаковые, то элемент добавляется в результатgit
def num_jewels_in_stones(J, S):
    jewels = 0

    for j in J:
        for s in S:
            if s == j:
                jewels += 1

    return jewels

print(num_jewels_in_stones("aA", "aAAbbbb"))
