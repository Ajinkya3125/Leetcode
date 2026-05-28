##1160 : Find words that can be formed by the characters

from collections import Counter
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)
            if word_count & count == word_count:
                total_length += len(word)
        return total_length