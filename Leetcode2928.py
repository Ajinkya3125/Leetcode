#2928:Distribute Candies Among Children I

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(x):
            if x < 2:
                return 0
            return x * (x-1) // 2

        total = comb(n+2)

        total -= 3*comb(n-(limit+1)+2)

        total += 3*comb(n-2*(limit+1)+2)

        total -= comb(n-3*(limit+1)+2)

        return total