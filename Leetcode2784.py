##2784 : Check if array is Good

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False

        nums.sort()

        expected = list(range(1,n+1)) + [n]

        return nums == expected