##2574 : Left and Right sum differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        result = []

        for num in nums:
            total -= num  
            result.append(abs(left_sum - total))
            left_sum += num

        return result