#434:Number of segments in a string

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())