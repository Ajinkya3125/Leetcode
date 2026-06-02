##3633 : Earliest Finish Time for Land and Water Rides I

from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                water_finish = max(land_finish, waterStartTime[j]) + waterDuration[j]

                # Water -> Land
                water_finish2 = waterStartTime[j] + waterDuration[j]
                land_finish2 = max(water_finish2, landStartTime[i]) + landDuration[i]

                ans = min(ans, water_finish, land_finish2)

        return ans
        