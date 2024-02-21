# Concept:  #
# Walk all cities in a province first.
# Walk all array but return 0 if the city has been visited.
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        
        visited = set()
        def walk_all_cities(isConnected, visited, row):
            if row in visited:
                return 0
            visited.add(row)

            for col in range(COLS):
                if isConnected[row][col] == 1:
                    walk_all_cities(isConnected, visited, col)
            return 1
        provinces = 0
        for row in range(ROWS):
            provinces += walk_all_cities(isConnected, visited, row)
        return provinces