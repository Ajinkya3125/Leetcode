##748:shortest completing word

from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        # Step 1: Extract letters and count frequency
        license_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        result = None
        
        # Step 2: Check each word
        for word in words:
            word_count = Counter(word.lower())
            
            # Step 3: Check if word satisfies license plate condition
            if all(word_count[c] >= license_count[c] for c in license_count):
                
                # Step 4: Update shortest word
                if result is None or len(word) < len(result):
                    result = word
        
        return result