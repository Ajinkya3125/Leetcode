##442 : Find All duplicates elements in an array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)
        return result