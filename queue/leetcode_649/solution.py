import collections
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = collections.deque(senate)
        
        while len(queue) > 1:
            party = queue.popleft()
            try:
                queue.remove("R" if party == "D" else "D")
                queue.append(party)
            except:
                pass

        return "Dire" if queue.pop() == "D" else "Radiant"