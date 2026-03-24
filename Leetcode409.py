#409:Longest palindrome
#Given a string s which consists of lowercase or uppercase letters,
#return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        length = 0
        odd_found = False

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True

        if odd_found:
            length += 1

        return length