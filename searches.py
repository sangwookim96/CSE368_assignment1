''' 
Structure written by: Nils Napp
Solution by: Jiwon Choi (F18 HW script)
'''
import time
from slideproblem import *
from collections import *
import heapq
# you likely need to inport some more modules to do the serach
# for deque

"""returns a list of nodes that are children of the node n.
n: Node, p: Problem"""


def _expand(n: Node, p: Problem):
    # Node n's state
    n_state = n.state
    # action list of n's applicable actions
    n_applicable_actions = p.applicable(n_state)

    # cnlist: child node list.
    cnlist = []
    for ai in n_applicable_actions:
        child_i = child_node(n, ai, p)
        cnlist.append(child_i)

    return cnlist


class Searches:
    def graph_bfs(self, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        # parent=None, action=None, cost=0, state=initialState
        node = Node(None, None, 0, problem.initialState)
        if problem.goalTest(node.state):
            return node
        # initial frontier has a node with initial state (node)
        # frontier: FIFO queue. Left is the head. Right is the tail. List of nodes.
        frontier = deque([node])
        # set() contains distinct items (state).
        # required for graph search.
        explored = set()
        # search begin
        while frontier:
            node = frontier.popleft()
            # turn node state to tuple for pushing in the explored node set.
            node_state_tuple = node.state.toTuple()
            explored.add(node_state_tuple)
            for child in _expand(node, problem):
                if child.state.toTuple() not in explored and child not in frontier:
                    if problem.goalTest(child.state):
                        return solution(child)
                    frontier.append(child)

        return "Fake return value"

    def recursiveDL_DFS(self, lim, problem):
        n = Node(None, None, 0, problem.initialState)
        return self.depthLimitedDFS_for_id_dfs(n, lim, problem)

    def depthLimitedDFS(self, n, lim, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        if problem.goalTest(n.state):
            return solution(n)
        elif lim == 0:
            return None

        for child in _expand(n, problem):
            result = self.depthLimitedDFS(child, lim-1, problem)
            if result != None:
                return result
        return None

    def depthLimitedDFS_for_id_dfs(self, n, lim, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        if problem.goalTest(n.state):
            return n
        elif lim == 0:
            return None

        for child in _expand(n, problem):
            result = self.depthLimitedDFS_for_id_dfs(child, lim-1, problem)
            if result != None:
                return result
        return None

    def id_dfs(self, problem):
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        maxDepth = 30
        for d in range(maxDepth):
            result = self.recursiveDL_DFS(d, problem)
            if result != None:
                return solution(result)

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
        node = Node(None, None, 0, problem.initialState)
        frontier = [node]
        heapq.heapify(frontier)
        while frontier:
            node = heapq.heappop(frontier)
            if node.state == problem.goalState:
                return solution(node)

            for child in _expand(node, problem):
                child.f = child.cost + \
                    self.heuristic(child.state, problem.goalState)
                frontier.append(child)

        return None

    def a_star_graph(self, problem: Problem) -> tuple:
        # reset the node counter for profiling
        # the serach should return the result of 'solution(node)'
        "*** YOUR CODE HERE ***"
        node = Node(None, None, 0, problem.initialState)
        frontier = [node]
        heapq.heapify(frontier)
        explored = set()
        while frontier:
            node = heapq.heappop(frontier)
            if node.state == problem.goalState:
                return solution(node)
            nodeState = tuple(node.state.toTuple())
            explored.add(nodeState)

            for child in _expand(node, problem):
                child.f = child.cost + \
                    self.heuristic(child.state, problem.goalState)
                frontier.append(child)

        return None

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

    print("This is initialState before 15 random moves")
    print(p.initialState)

    si = State(s)
    # change the number of random moves appropriately
    # If you are curious see if you get a solution >30 moves. The
    apply_rnd_moves(15, si, p)
    print("This is si (or future initialState) after 15 random moves")
    print(si)
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
