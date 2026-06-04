#1816 : Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        return " ".join(words[:k])