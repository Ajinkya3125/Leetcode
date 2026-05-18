##804 : Unique Morse Code Words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]
        
        transformations = set()
        
        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            transformations.add(code)
        
        return len(transformations)