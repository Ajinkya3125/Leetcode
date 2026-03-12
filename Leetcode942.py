#942:DI string match
#A permutation perm of n + 1 integers of all the integers in the range [0, n]
#  can be represented as a string s of length n where:
#s[i] == 'I' if perm[i] < perm[i + 1], and
#s[i] == 'D' if perm[i] > perm[i + 1].
#Given a string s, reconstruct the permutation perm and return it.
#If there are multiple valid permutations perm, return any of them.

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        result = []

        for i in s:
            if i == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result