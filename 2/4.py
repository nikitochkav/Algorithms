from typing import List
"""Сложность данной функции O(n*m).
        """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0 # Проходит элемент через цикл
        for i in range(1, len(prices)):    # Проверяет больше ли цена на i
            if prices[i] > prices[i-1]:    # Добавляет разницу к прибыли и увеличивает ее
                maximumProfit += prices[i] - prices[i-1]
        return maximumProfit        # Возвращает максимальную прибыль