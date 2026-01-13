class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        for x in basket1:
            cnt[x] += 1
        for x in basket2:
            cnt[x] -= 1
        swaps = []
        for fruit, diff in cnt.items():
            if diff % 2 != 0:
                return -1
            for _ in range(abs(diff) // 2):
                swaps.append(fruit)
        swaps.sort()
        min_fruit = min(min(basket1), min(basket2))
        n = len(swaps)
        cost = 0
        for i in range(n // 2):
            cost += min(swaps[i], 2 * min_fruit)
        return cost