##1374 : Generate a string with Characters that have Odd counts.

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "a" * n
        else:
            return "a" * (n-1) + "b"