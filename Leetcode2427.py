#2427:Number of Common Factors
#Given two positive integers a and b, return the number of common factors of a and b.
#An integer x is a common factor of a and b if x divides both a and b.

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cnt = 0
        for i in range(1,min(a,b)+1):
            if a % i == 0 and b % i == 0:
                cnt += 1
        return cnt