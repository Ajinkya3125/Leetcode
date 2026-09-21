from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            # Subarray containing only num
            new_dp[r] += 1

            # Extend previous subarrays
            for rem in range(k):
                if dp[rem]:
                    new_dp[(rem * r) % k] += dp[rem]

            dp = new_dp

            for rem in range(k):
                ans[rem] += dp[rem]

        return ans