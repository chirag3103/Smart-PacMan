# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
      #frontier = getStartState();
    #inside while loop
        #frontier = getSuccessors(frontier)
        #if frontier is empty
            #return false
        #else choose the last node from the stack and pop it from the frontier
        #if that node contains a solution
            #return solution
        #else exapand that node and push all neighbours into the frontier

	
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    from stackfile import Mystack
    Mystack.mystack.append(problem.getStartState())
    Mystack.mystack.append(problem.getSuccessors(problem.getStartState()))
    print Mystack.mystack
    
    
    frontier=[]
    startposition = problem.getStartState()
    frontier.append(startposition)
    actions=[]
     #frontier.append(problem.getSuccessors(frontier))
    print frontier
    lst=[]
    node =util.Stack()
    lst.append(startposition)
    condition = True
    while condition is True:
        node=lst.pop()
        lst.append(node)
        for i in problem.getSuccessors(node):
            if i[0] not in lst:
                lst.append(i[0])
                actions.append(i[1])
                print "appened..",i
        node=lst.pop()
        actions.pop()
        print "popped node is",node
        if problem.isGoalState(node):
            print "Goal node is",node
            condition = False
            break
        else:
            node=lst.pop()
            lst.append(node)
            for i in problem.getSuccessors(node):
                if i[0] not in lst:
                    lst.append(i[0])
                    actions.append(i[1])
                    print "appened....",i
        print "list ",lst
        print "actions",actions
        node=lst.pop()
        if problem.isGoalState(node):
            print "Goal node is",node
            condition=False
        # break

    for i, word in enumerate(actions):
        move(actions[i])
    #print "popped node is",lst.pop()
    #print actions
    return factions
    """
    """
    #Sample
    frontiernode = util.Stack()
    visitednode = []
    actions = []
    initialstate=problem.getStartState()
    #creating a tuple datastructure to store the all details of a node
    startNode = (initialstate, None, actions)
    #explicit formatting of frontiernode stack into a tuple format
    frontiernode.push(startNode)
    #done so that we can get the particular data regarding location, direction and weight
    while not frontiernode.isEmpty():
        currentnode = frontiernode.pop()
        #getting the first position data that is the location in the grid
        currentLocation = currentnode[0]
        #getting the second position data that is the direction
        currentDirection = currentnode[1]
        #getting the third position data that is the weight for traversing
        currentPath = currentnode[2]
        #checking for the entry of that node in a visited nodes list
        if(currentLocation not in visitednode):
            #if not then appennding into the list
            visitednode.append(currentLocation)
            #checking for the goal state
            if(problem.isGoalState(currentLocation)):
                #if found then returning the path till that node
                return currentPath
            #if not then getting the successors of that node
            successors = problem.getSuccessors(currentLocation)
            #creating a list of the successors by adding the current node successors
            #creating a list also because we can parse the list and check positions
            successorsList = list(successors)
            #checking the successor list before adding it to the frontier
            for i in successorsList:
                #checking the position in visited node list
                if i[0] not in visitednode:
                    #only if not then pushing it to the stack
                    #path variable is evaluated for calculating the expense to reach
                    frontiernode.push((i[0], i[1], currentPath + [i[1]]))
    return actions
    

    node = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()): return node.solution()
    frontier = util.Stack()
    frontier.push(node)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node.state): return node.solution()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored:
                frontier.push(child)
    return []
    """

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    theFringe = util.Stack()
    expanded = set()
    theFringe.push((problem.getStartState(),[]))

    while not theFringe.isEmpty():
        popState, popMoves = theFringe.pop()
        if(popState in expanded):
            continue
        if problem.isGoalState(popState):
            return popMoves
        expanded.add(popState)
        for state, direction, cost in problem.getSuccessors(popState):
            if(state in expanded):
                continue
            theFringe.push((state, popMoves+[direction]))
    return []




    #util.raiseNotDefined()




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """
    frontier = util.Queue()
    visited = []
    startNode = (problem.getStartState(), None, [])
    frontier.push(startNode)
    while not frontier.isEmpty():
        curr = frontier.pop()
        currLoc = curr[0]
        currDir = curr[1]
        currPath = curr[2]
        if(currLoc not in visited):
            visited.append(currLoc)
            if(problem.isGoalState(currLoc)):
                return currPath
            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)
            for i in successorsList:
                if i[0] not in visited:
                    frontier.push((i[0], i[1], currPath + [i[1]]))
    return []
    

    node = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()): return node.solution()
    frontier = util.Queue()
    frontier.push(node)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node.state): return node.solution()
        explored.add(node.state)
        for child in node.expand(problem):
            if (child.state not in explored) and (child not in frontier.list):
                frontier.push(child)
    return []
    """
    theFringe = util.Queue()
    expanded = set()
    theFringe.push((problem.getStartState(),[]))

    while not theFringe.isEmpty():
        popState, popMoves= theFringe.pop()
        if(popState in expanded):
            continue
        if problem.isGoalState(popState):
            return popMoves
        expanded.add(popState)
        for state, direction, cost in problem.getSuccessors(popState):
            if(state in expanded):
                continue
            theFringe.push((state, popMoves+[direction]))
    return []





    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """    
    frontier = util.PriorityQueue()
    visited = []
    startNode = ((problem.getStartState(), None, 0), [], 0)
    frontier.push(startNode, None)
    while not frontier.isEmpty():
        curr = frontier.pop()
        currLoc = curr[0][0]
        currDir = curr[0][1]
        currPath = curr[1]
        currCost = curr[2]
        if currLoc not in visited:
            visited.append(currLoc)
            if(problem.isGoalState(currLoc)):
                return currPath
            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)
            for i in successorsList:
                if i[0] not in visited:
                    if(problem.isGoalState(i[0])):
                        return currPath + [i[1]]
                    newNode = (i, currPath+[i[1]], currCost + i[2])
                    frontier.push(newNode, currCost + i[2])
    return []
    
    
    
    node = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()): return node.solution()
    frontier = util.PriorityQueue()
    frontier.push(node, node.path_cost)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node.state): return node.solution()
        explored.add(node.state)
        for child in node.expand(problem):
            if ((child.state not in explored) and (child not in frontier.heap)):
                frontier.push(child, child.path_cost)
    """
    theFringe = util.PriorityQueue()
    expanded = set()
    theFringe.push((problem.getStartState(),[],0),0)

    while not theFringe.isEmpty():
        
        popState, popMoves, popCost = theFringe.pop()
        #print popCost
        #print "Expanding ", popState
        if(popState in expanded):
            continue

        if problem.isGoalState(popState):
            return popMoves

        expanded.add(popState)

        for state, direction, cost in problem.getSuccessors(popState):
            if(state in expanded):
                continue
            theFringe.push((state, popMoves+[direction], popCost+cost),popCost+cost)
            #print popCost+cost
            #print "Inside-push",state
    return []



    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """
    frontier = util.PriorityQueue()
    visited = []
    h = heuristic(problem.getStartState(), problem)
    g = 0
    f = g + h
    startingNode = (problem.getStartState(), None, g, [])
    frontier.push(startingNode, f)
    while not frontier.isEmpty():
        curr = frontier.pop()
        currLoc = curr[0]
        currDir = curr[1]
        currCost = curr[2]
        if currLoc not in visited:
            currPath = curr[3]
            visited.append(currLoc)
            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)
            for i in successorsList:
                if i[0] not in visited:
                    if(problem.isGoalState(i[0])):
                        return currPath + [i[1]]
                h = heuristic(i[0], problem)
                g = currCost + i[2]
                f = g + h
                newNode = (i[0], i[1], g, currPath+[i[1]])
                frontier.push(newNode, f)
    return []
    
    node = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()): return node.solution()
    frontier = util.PriorityQueue()
    frontier.push(node, node.path_cost+heuristic(node.state, problem))
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node.state): return node.solution()
        explored.add(node.state)
        for child in node.expand(problem):
            if (child.state not in explored) and (child not in frontier.heap):
                frontier.push(child, child.path_cost+heuristic(child.state, problem))
    #util.raiseNotDefined()
    """
    theFringe = util.PriorityQueue()
    expanded = set()
    theFringe.push((problem.getStartState(),[],0),0)

    while not theFringe.isEmpty():
        
        currentState, currentMoves, currentCost = theFringe.pop()
        if(currentState in expanded):
            continue

        if problem.isGoalState(currentState):
            return currentMoves
        
        expanded.add(currentState)

        for state, direction, cost in problem.getSuccessors(currentState):
            if(state in expanded):
                continue
            hvalue = heuristic(state, problem)
            theFringe.push((state, currentMoves+[direction], currentCost+cost),currentCost+cost+hvalue)
    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
