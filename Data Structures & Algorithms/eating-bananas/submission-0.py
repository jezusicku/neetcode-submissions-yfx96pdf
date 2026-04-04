import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(k: int) -> bool:
            total = 0
            for p in piles:
                total = total + math.ceil(p/k)
            if total <= h:
                return True
            return False

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) //2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left