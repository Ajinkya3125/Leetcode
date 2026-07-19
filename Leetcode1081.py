class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {}

        # Store the last occurrence of each character
        for i, ch in enumerate(s):
            last_index[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):
            if ch in visited:
                continue

            # Remove larger characters if they appear later
            while stack and ch < stack[-1] and last_index[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)