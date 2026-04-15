#2515:Shortest Distance to Target string In a Circular Array

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        
        for i in range(n):
            if words[i] == target:
                forward = (i - startIndex) % n
                backward = (startIndex - i) % n
                ans = min(ans, forward, backward)
        
        return ans if ans != float('inf') else -1