#2678 : Number of Senior Citizens

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for person in details:
            age = int(person[11:13])
            if age > 60:
                cnt += 1
        return cnt