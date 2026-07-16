class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        ans = ""

        while len(s) > 3:
            ans = "." + s[-3:] + ans
            s = s[:-3]

        return s + ans