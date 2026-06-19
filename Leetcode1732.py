#1732 : Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = highest = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest