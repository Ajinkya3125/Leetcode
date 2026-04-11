#914: X of a Kind in a Deck of cards

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = {}
        #count manually
        for card in deck:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1
        values = list(freq.values())

        ##Try possible group sizes
        min_count = min(values)

        for x in range(2,min_count+1):
            valid = True
            for v in values:
                if v % x != 0:
                    valid = False
                    break
            if valid:
                return True
        return False 