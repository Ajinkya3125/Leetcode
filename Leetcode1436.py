##1436 : Destination City

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set()

        for a, b in paths:
            start_cities.add(a)

        for a,b in paths:
            if b not in start_cities:
                return b