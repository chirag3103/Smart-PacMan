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
    "*** YOUR CODE HERE ***"    
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    """
    #created a frontier Stack for DFS
    #Here the stack acts as a LIFO stack
    neighbourNodes = util.Stack()
    #created a list of moves which will be returned in then end
    moves = []
    #pushed the start node and empty moves list, onto the frontier stack
    neighbourNodes.push((problem.getStartState(),moves))
    #this is a set of nodes which have been seen, to avoid adding nodes already visited 
    seenNodes = set()
    #condition evaluated based on the existence of elements in the frontier stack
    while not neighbourNodes.isEmpty():
        #last node in the stack is popped and its state and action is stored
        poppedNodeState, poppedNodeAction = neighbourNodes.pop()
        #condition to check if the node is already been visited
        if(poppedNodeState in seenNodes):
            #if yes then it just skips the iteration using the continue statement
            continue
        #condition to check if the current node is the goal node
        if problem.isGoalState(poppedNodeState):
            #if yes then return the action or moves to be performed list
            return poppedNodeAction
        #if not visited before then node is added to the seenNodes set
        seenNodes.add(poppedNodeState)
        #loop to parse the successor nodes and check and add them to the frontier stack
        for state, action, cost in problem.getSuccessors(poppedNodeState):
            #checking if the successor node has already been visited before
            if(state in seenNodes):
                #if yes then it skips that node
                continue
            #else it adds that successor along with it action appeneded with the already existing actions
            neighbourNodes.push((state, poppedNodeAction+[action]))
    #the list of moves if finally returned
    return moves
    #util.raiseNotDefined()
    """
    neighbourNodes = util.Stack()
    moves = []
    neighbourNodes.push((problem.getStartState(),moves))
    seenNodes = set()
    while not neighbourNodes.isEmpty():
        poppedNodeState, poppedNodeAction = neighbourNodes.pop()
        if(poppedNodeState in seenNodes):
            continue
        if problem.isGoalState(poppedNodeState):
            return poppedNodeAction
        seenNodes.add(poppedNodeState)
        for state, action, cost in problem.getSuccessors(poppedNodeState):
            if(state in seenNodes):
                continue
            neighbourNodes.push((state, poppedNodeAction+[action]))
    return moves    
 



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #the logic is same as for DFS just that i made use of a Queue data structure
    #Here the queue acts as a FIFO queue
    neighbourNodes = util.Queue()
    moves = []
    neighbourNodes.push((problem.getStartState(),moves))
    seenNodes = set()

    while not neighbourNodes.isEmpty():
        poppedNodeState, poppedNodeAction= neighbourNodes.pop()
        if(poppedNodeState in seenNodes):
            continue
        if problem.isGoalState(poppedNodeState):
            return poppedNodeAction
        seenNodes.add(poppedNodeState)
        for state, action, cost in problem.getSuccessors(poppedNodeState):
            if(state in seenNodes):
                continue
            neighbourNodes.push((state, poppedNodeAction+[action]))
    return moves
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #the logic is pretty much the same just that, unlike the other two algorithms we take it consideration cost of every node
    #created a priority queue for the frontier nodes
    neighbourNodes = util.PriorityQueue()
    moves = []
    #hence while pushing into the queue, there are three tuples (state,action,cost)
    neighbourNodes.push((problem.getStartState(),moves,0),0)
    seenNodes = set()

    while not neighbourNodes.isEmpty():
        poppedNodeState, poppedNodeAction, popCost = neighbourNodes.pop()
        if(poppedNodeState in seenNodes):
            continue
        if problem.isGoalState(poppedNodeState):
            return poppedNodeAction
        seenNodes.add(poppedNodeState)
        for state, action, cost in problem.getSuccessors(poppedNodeState):
            if(state in seenNodes):
                continue
            #here, when a node is pushed into the piority queue, the actions are appeneded as usual
            #but also the cost is addede, so tht we know what is the cost of visting the node
            neighbourNodes.push((state, poppedNodeAction+[action], popCost+cost),popCost+cost)
    return moves
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
    #here again we are making use of the priority queue for storing the frontier nodes
    #created a priority queue for Astarsearch
    neighbourNodes = util.PriorityQueue()
    moves = []
    neighbourNodes.push((problem.getStartState(),moves,0),0)
    seenNodes = set()

    while not neighbourNodes.isEmpty():
        currentState, currentActions, currentCost = neighbourNodes.pop()
        if(currentState in seenNodes):
            continue
        if problem.isGoalState(currentState):
            return currentActions
        seenNodes.add(currentState)
        for state, action, cost in problem.getSuccessors(currentState):
            if(state in seenNodes):
                continue
            #here we calculate the hueristic value of visting each nodes
            hvalue = heuristic(state, problem)
            #and while pushing onto the queue we not only have the cost to visit the node
            #but also the heuristic value of that node.
            neighbourNodes.push((state, currentActions+[action], currentCost+cost),currentCost+cost+hvalue)
    return moves

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
