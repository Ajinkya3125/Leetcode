##2363 : Merge Similar Items

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}

        for value, weight in items1:
            d[value] = d.get(value, 0) + weight

        for value, weight in items2:
            d[value] = d.get(value, 0) + weight

        result = []

        for value in sorted(d):
            result.append([value, d[value]])

        return result