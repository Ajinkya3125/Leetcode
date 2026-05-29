##3300 : Minimum Element After Replacement With Digit Sum

class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = float('inf')
        
        for n in nums:
            digit_sum = 0
            
            while n > 0:
                digit_sum += n % 10
                n //= 10
            
            mini = min(mini, digit_sum)
        
        return mini