from collections import defaultdict
import collections
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])

        def in_graph(row, col):
            return True if (row > -1 and
                            col > -1 and 
                            row < ROWS and 
                            col < COLS) else False
        def meet_border(row, col):
            return True if (row == 0 or
                            col == 0 or
                            row == ROWS -1 or
                            col == COLS -1) else False
        
        row, col = entrance

        queue = collections.deque()
        visited = defaultdict(list)
        visited[row] = [col]
        queue.append([row + 1, col, visited, 1])
        queue.append([row - 1, col, visited, 1])
        queue.append([row, col + 1, visited, 1])
        queue.append([row, col - 1, visited, 1])
        
        while queue:
            que_len = len(queue)
            
            for _ in range(que_len):
                row_, col_, visited, steps = queue.popleft()

                if (meet_border(row_, col_) and 
                    in_graph(row_, col_) and
                    maze[row_][col_] == "." and
                    (row_, col_) != (row, col)):
                    return steps
                elif (not in_graph(row_, col_) or
                    maze[row_][col_] == "+" or 
                    col_ in visited[row_]):
                    pass
                else:
                    visited[row_].append(col_)
                    steps += 1
                    queue.append([row_ + 1, col_, visited, steps])
                    queue.append([row_ - 1, col_, visited, steps])
                    queue.append([row_, col_ + 1, visited, steps])
                    queue.append([row_, col_ - 1, visited, steps])

        return -1