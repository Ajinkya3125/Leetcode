##1446 : Consecutive Characters

class Solution:
    def maxPower(self, s: str) -> int:
        max_count = 1
        curr_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                curr_count = 1

            max_count = max(max_count, curr_count)

        return max_count