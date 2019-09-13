''' 
Structure written by: Nils Napp
Solution by: Jiwon Choi (F18 HW script)
'''
import time
from slideproblem import *
# you likely need to inport some more modules to do the serach
# for deque
from collection import *


class Searches:
    def graph_bfs(self, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        node = Node(problem.initialState)

        return "Fake return value"

    def recursiveDL_DFS(self, lim, problem):
        n = Node(None, None, 0, problem.initialState)
        return self.depthLimitedDFS(n, lim, problem)

    def depthLimitedDFS(self, n, lim, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        return "Fake return value"

    def id_dfs(self, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        return "Fake return value"

    # START: DEFINED ALREADY
    def poseList(self, s):
        poses = list(range(s.boardSize*s.boardSize))

        for tile in range(s.boardSize*s.boardSize):
            for row in range(s.boardSize):
                for col in range(s.boardSize):
                    poses[s.board[row][col]] = [row, col]
        return poses

    def heuristic(self, s0, sf):
        pl0 = self.poseList(s0)
        plf = self.poseList(sf)

        h = 0
        for i in range(1, s0.boardSize*s0.boardSize):
            h += abs(pl0[i][0] - plf[i][0]) + abs(plf[i][1] - plf[i][1])
        return h
    # END: DEFINED ALREADY

    def a_star_tree(self, problem: Problem) -> tuple:
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        return "Fake return value"

    def a_star_graph(self, problem: Problem) -> tuple:
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        return "Fake return value"

    # EXTRA CREDIT (OPTIONAL)
    def solve4x4(self, p: Problem) -> tuple:
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        return "Fake return value"


if __name__ == '__main__':
    p = Problem()
    s = State()
    n = Node(None, None, 0, s)
    n2 = Node(n, None, 0, s)

    searches = Searches()

    # goalState of the Problem is the Problem's initial state.
    p.goalState = State(s)

    # mix up the problem.
    p.apply('R', s)
    p.apply('R', s)
    p.apply('D', s)
    p.apply('D', s)
    p.apply('L', s)

    p.initialState = State(s)

    print(p.initialState)

    si = State(s)
    # change the number of random moves appropriately
    # If you are curious see if you get a solution >30 moves. The
    apply_rnd_moves(15, si, p)
    p.initialState = si

    startTime = time.perf_counter()

    print('\n\n=== BFS ===\n')
    startTime = time.perf_counter()
    res = searches.graph_bfs(p)
    print(time.perf_counter()-startTime)
    print(Node.nodeCount)
    print(res)

    print('\n\n=== Iterative Deepening DFS ===\n')
    startTime = time.perf_counter()
    res = searches.id_dfs(p)
    print(time.perf_counter()-startTime)
    print(Node.nodeCount)
    print(res)

    print('\n\n=== A*-Tree ===\n')
    startTime = time.perf_counter()
    res = searches.a_star_tree(p)
    print(time.perf_counter()-startTime)
    print(Node.nodeCount)
    print(res)

    print('\n\n=== A*-Graph ===\n')
    startTime = time.perf_counter()
    res = searches.a_star_graph(p)
    print(time.perf_counter()-startTime)
    print(Node.nodeCount)
    print(res)

    # EXTRA CREDIT (OPTIONAL)
    # UN-COMMENT the code below when you test this
    # change the 'boardSize' variable into 4 from slideproblem.py file
    """
    print('\n\n=== A*-solve4x4 ===\n')
    startTime = time.clock()
    res = searches.solve4x4(p)
    print(time.clock() - startTime)
    print(Node.nodeCount)
    print(res)
    """
