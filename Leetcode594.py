##594 : Longest Harmonious Subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(nums)
        longest = 0
        
        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])
        
        return longest