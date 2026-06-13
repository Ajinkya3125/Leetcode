#3838 : Weighted Word Mapping

from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            total %= 26

            result += chr(ord('a') + (25 - total))

        return result