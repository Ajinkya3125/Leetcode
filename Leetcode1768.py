##1768:Merge strings alternately.

#You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        ans = ""
        i = 0
        j = 0
        while(i < n and j < m):
            ans = ans + word1[i]
            ans = ans + word2[j]
            i += 1
            j += 1
        ans = ans + word1[i:]
        ans = ans + word2[j:]
        return ans