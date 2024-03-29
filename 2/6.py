Функция проходит по списку чисел и находит максимальную сумму кражи, избегая ограбления двух соседних домов
Сложность алгоритма: O(n), где n - количество элементов в списке цен на акции
"""


def check(nums):
    rob = 0             # дом, который можно грабить
    skip = 0            # дом, кторый пропускаем
    for num in nums:
        rob, skip = skip + num, max(rob, skip)  # в rob заносим текущую сумму + skip, в skip максимальное из skip и rob
    return max(rob, skip)


def rob(nums):
    if len(nums) == 1:      # если длина списка = 1, возвращаем единственные эл-нт
        return nums[0]
    elif not nums:          # если на ввод дано пустое множество, возвращаем 0
        return 0
    else:
        return max(check(nums[1:]), check(nums[:-1]))   # возвращаем макс из предыдущей функции при разных срезах
