##2309 : Greatest English Letter in Upper and Lower case

class Solution:
    def greatestLetter(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch.isupper() and ch.lower() in s:
                result = max(result, ch)

        return result