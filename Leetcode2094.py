#2094: Finding 3-Digit Even numbers.

from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            temp = Counter(map(int, str(num)))

            if all(temp[d] <= count[d] for d in temp):
                result.append(num)

        return result