class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        if len(rooms[0]) == 0:
            return False if len(rooms) > 1 else True

        self.keys = set(rooms[0])
        self.visited = set([0])

        while self.keys:
            key = self.keys.pop()
            if key in self.visited:
                continue
            else:
                self.visited.add(key)
                for k in rooms[key]:
                    self.keys.add(k)
        return len(rooms) == len(self.visited)