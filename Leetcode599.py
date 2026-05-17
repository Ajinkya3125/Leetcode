##599 : Minimum Index sum of two lists.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {restaurant: i for i, restaurant in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        for j, restaurant in enumerate(list2):
            if restaurant in d:
                total = d[restaurant] + j
                
                if total < min_sum:
                    min_sum = total
                    result = [restaurant]
                elif total == min_sum:
                    result.append(restaurant)
        
        return result