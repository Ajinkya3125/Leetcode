#506:Relative Ranks

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # Pair score with index
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        
        result = [""] * len(score)
        
        for rank, (s, idx) in enumerate(sorted_scores):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result