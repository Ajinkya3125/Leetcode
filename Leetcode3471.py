from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()

        for i in range(n - k + 1):
            window = set(nums[i:i + k])

            for num in window:
                count[num] += 1

        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans