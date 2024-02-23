import pdb
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        reachable = set([0])
        reorder = 0
        stack = []
        while connections:
            a, b = connections.pop()
            if b in reachable:
                reachable.add(a)
            elif a in reachable:
                reachable.add(b)
                reorder += 1
            else:
                stack.append([a, b])
            if len(connections) == 0:
                connections = stack
                stack = []
        return reorder

        # self.res = 0
        # road_to_city_0 = set([0])
        # for city in connections:
        #     if city[1] == 0:
        #         road_to_city_0.add(city[0])
        #         connections.remove(city)
        #     elif city[0] == 0:
        #         self.res += 1
        #         road_to_city_0.add(city[1])
        #         connections.remove(city)
        
        # while len(road_to_city_0) != n:
        #     for city in connections:
        #         if city[1] in road_to_city_0:
        #             road_to_city_0.add(city[0])
        #             connections.remove(city)
        #         elif city[0] in road_to_city_0:
        #             self.res += 1
        #             road_to_city_0.add(city[1])
        #             connections.remove(city)
                
        # return self.res