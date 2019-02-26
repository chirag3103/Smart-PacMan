# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """
    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #considering both the food and the ghost location for the best reflex agent
        
        foodParticleList = currentGameState.getFood().asList()
        
        #initializing the distance to a positive max in the beginning
        initDistance = float('inf')
        
        #loop for parsing through all the food particles in the created FoodList
        for presentFoodParticle in foodParticleList:
            #calculating the distance using the manhattanDistance method using the newPos variable 
            initDistance = min(initDistance,manhattanDistance(presentFoodParticle,newPos))
            #check if the current action is STOP
            if Directions.STOP in action:
                #if yes then return negative max value  
                return float('-inf')
        
        #loop for parsing through all the newGhostStates    
        for presentGhostState in newGhostStates:
            #get the current ghostState's location
            presentGhostLocation = presentGhostState.getPosition()
            #checking if the current ghost location matching with the pacman's position
            if presentGhostLocation == newPos:
                #if yes then returning the negative max value
                return float('-inf')
        
        #final return of reciprocal of distance
        return 1.0/(1.0 + initDistance)
        
        

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        movesList = self.MiniMax(gameState, 0, 0)
        return movesList[0]
        
    
    def minimum_Value(self,gameState, depth, agentsCount):
        #initial minimum value that is the action value pair
        
        #get the list of actions for the ghost
        ghostMovesList = gameState.getLegalActions(agentsCount)
        #initial move is nothing and value is set to max
        minimalVal = ["", float('inf')]
        #checking the ghostMoves list for not empty
        if not ghostMovesList:
            #if yes then return the minimax move of that current gameState
            return self.evaluationFunction(gameState)

        #parsing through the list of ghost moves
        for gMove in ghostMovesList:
            #getting the sucessor game state after performing the given move
            successorState = gameState.generateSuccessor(agentsCount, gMove)
            #calling the minOrmax function to get the moves list
            presentMoveList = self.MiniMax(successorState, depth, agentsCount + 1)
            #checking the returned move_list from minormax function 
            if type(presentMoveList) is not list:
                #if true then save the move in pMove
                pMove = presentMoveList
            else:
                #if not true then save the depth
                pMove = presentMoveList[1]
            #checking if the depth is less than the inital depth
            if pMove < minimalVal[1]:
                #if true then store new values in the minimal variable
                minimalVal = [gMove, pMove]
        #returning the final minimal value pair
        return minimalVal


    def maximum_Value(self,gameState, depth, agentsCount):
        #evereything remains the same except
        #initital max is set to negative max
        maximalVal = ["", float('-inf')]
        movesList = gameState.getLegalActions(agentsCount)

        if not movesList:
            return self.evaluationFunction(gameState)

        for move in movesList:
            successorState = gameState.generateSuccessor(agentsCount, move)
            presentMoveList = self.MiniMax(successorState, depth, agentsCount + 1)
            if type(presentMoveList) is not list:
                pMove = presentMoveList
            else:
                pMove = presentMoveList[1]
            #just the comparison condition changes here 
            if pMove > maximalVal[1]:
                maximalVal = [move, pMove]
        return maximalVal


    #function to return the minmum or maximum value as per evaluation
    def MiniMax(self,gameState, depth, agentsCount):
        #checking the index of agent with the current number of agents
        if agentsCount >= gameState.getNumAgents():
            depth += 1
            agentsCount = 0
            #checking if the current state to be a win or lose, or the depth to be completely explored
        if (gameState.isWin() or gameState.isLose() or depth == self.depth):
            #if any of these conditions is true, returning the current move from the current state
            return self.evaluationFunction(gameState)
        #checking the agent indexes
        elif (agentsCount != 0):
            #if not zero then minimum
            return self.minimum_Value(gameState, depth, agentsCount)
        else:
            #else maximum
            return self.maximum_Value(gameState, depth, agentsCount)
        
        
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        movesList=self.MiniMax(gameState,0,0,float('-inf'), float('inf'))
        #returning the move according to the current game state
        return movesList[0]

    def minimum_Value(self,gameState, height, agentsCount, temp1, temp2):
        minimalVal = ["", float('inf')]
        ghostMovesList = gameState.getLegalActions(agentsCount)

        if not ghostMovesList:
            return self.evaluationFunction(gameState)

        for gMove in ghostMovesList:
            successorState = gameState.generateSuccessor(agentsCount, gMove)
            presentMoveList = self.MiniMax(successorState, height, agentsCount + 1, temp1, temp2)

            if type(presentMoveList) is list:
                pMove = presentMoveList[1]
            else:
                pMove = presentMoveList

            #if there is a value smaller than value in the list
            if pMove < minimalVal[1]:
                #if yes then minval is reset with the new values                    
                minimalVal = [gMove, pMove]
            #if there is a value smaller than the passed value
            if pMove < temp1:
                #if yes then return the newly set values                    
                return [gMove, pMove]
            #else reset the values of the move with the new min amongst the two                
            temp2 = min(temp2, pMove)
        #returning the min value
        return minimalVal


    def maximum_Value(self,gameState, height, agentsCount, temp1, temp2):
        maximalVal = ["", float('-inf')]
        movesList = gameState.getLegalActions(agentsCount)

        if not movesList:
            return self.evaluationFunction(gameState)

        for move in movesList:
            successorState = gameState.generateSuccessor(agentsCount, move)
            presentMoveList = self.MiniMax(successorState, height, agentsCount + 1, temp1, temp2)

            if type(presentMoveList) is list:
                pMove = presentMoveList[1]
            else:
                pMove = presentMoveList

            #if there is a value greater than value in the list
            if pMove > maximalVal[1]:
                #if yes then maxval is reset with the new values
                maximalVal = [move, pMove]
            #if there is a value greater than the passed value
            if pMove > temp2:
                #if yes then return the newly set values
                return [move, pMove]
            #else reset the values of the move with the new max amongst the two
            temp1 = max(temp1, pMove)
        #returning the max value
        return maximalVal


    def MiniMax(self,gameState, height, agentsCount, temp1, temp2):
        #checking the number of agents at the given game state
        if agentsCount >= gameState.getNumAgents():
            #if yes then counter is set to zero
            agentsCount = 0
            #and depth of the tree if incremented by one
            height += 1
        #checking th present game state for a win or lose or the depth
        if (gameState.isWin() or gameState.isLose() or height == self.depth):
            #if yes then return the gamestate to the evaluation function
            return self.evaluationFunction(gameState)
        #check the number of agents
        elif (agentsCount != 0):
            #if not zero then returning min value function
            return self.minimum_Value(gameState, height, agentsCount, temp1, temp2)
        else:
            #if yes then retrurning the max value function
            return self.maximum_Value(gameState, height, agentsCount, temp1, temp2)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """


    def maximum_Value(self, gameState, agentsCount, height):
        #checking th present game state for a win or lose or the depth
        if (gameState.isWin() or gameState.isLose() or height == self.depth):
            #if yes then return the gamestate to the evaluation function
            return self.evaluationFunction(gameState)
        #set the initial max val to negative max
        maximalVal = float('-inf')
        #set the max move to 'stop'
        maximalMoveValue = "Stop"
        #get the list of moves
        movesList = gameState.getLegalActions(agentsCount)

        #parsing over the list of moves
        for move in movesList:
            #if move is stop then skip the loop
            if move == Directions.STOP:
                continue
            #else get the successor state
            successorState = gameState.generateSuccessor(agentsCount, move)
            #and call the max function to get the expected max
            temp1 = self.ExpectedMax(successorState, agentsCount+1, height)
            #compare the expeccted max with out local max value
            if temp1 > maximalVal:
                #exchange the values
                maximalVal = temp1
                maximalMoveValue = move
        #check the depth of the tree
        if height != 0:
            return maximalVal
        else:
            return maximalMoveValue

    def expected_Value(self, gameState, agentsCount, height):

        if (gameState.isWin() or gameState.isLose() or height == self.depth):
            return self.evaluationFunction(gameState)
    
        expectedValue = 0
        movesList = gameState.getLegalActions(agentsCount)

    
        probValue = 1.0/len(movesList)
        #parsing over the moves in the list
        for move in movesList:
            #if move is a stop, skip the loop
            if move == Directions.STOP:
                continue
            #get the successor state
            successorState = gameState.generateSuccessor(agentsCount, move)
            #call the expected max function
            temp1 = self.ExpectedMax(successorState, agentsCount+1, height)
            #compute the expected value
            expectedValue = expectedValue + (temp1 * probValue)
    
        return expectedValue

    def ExpectedMax (self, gameState, agentsCount, height):
        #check the number of agent of the current game state
        if agentsCount >= gameState.getNumAgents():
            height += 1
            agentsCount = 0
        #check the depth of the tree
        if height == self.depth:
            #if equal then calling the evaluate function for the current game state
            return self.evaluationFunction(gameState)
        #condition for number of agent
        if agentsCount != self.index:
            return self.expected_Value(gameState, agentsCount, height)
        else:
            return self.maximum_Value(gameState, agentsCount, height)

        return 'None'



    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        return self.ExpectedMax(gameState,0,0)


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION:
      comments are mentioned for explaining each step
    """
    "*** YOUR CODE HERE ***"
    #get the lists of ghost states 
    GhostStatesList = currentGameState.getGhostStates()
    #get the lists of capsule states
    CapsulesStatesList = currentGameState.getCapsules()
    #get the pacman position first
    presentPacPos = currentGameState.getPacmanPosition()
    #get the number of food given the current game state
    presentFoodParticleCount = currentGameState.getNumFood()
    #get the game score for the given game state
    presentGameScore = currentGameState.getScore()
    #evaluating the food particles left
    foodParticleLeft = 1.0/(presentFoodParticleCount + 1.0)
    #set initial ghost distance to max
    ghostDistance = float('inf')

    # print curScaredTimes
    #loop for parsing through the ghostStates
    for presentghostState in GhostStatesList:
        #getting the position of the current ghost state
        presentGhostPos = presentghostState.getPosition()
        #if the the pacman's current position is same as the ghost's current position or not
        if (presentPacPos != presentGhostPos):
            #if not then the manhattan distance between pacman's and ghost's current position is
            #compared with the staged value and stored as the new ghost distance
            ghostDistance = min(ghostDistance,manhattanDistance(presentPacPos,presentGhostPos))
        else:
            #returns a failure which is negatice max
            return float('-inf')
        #evaluating the inverse of the ghostdistance based on the lens of current
        #ghost states and storing it again 
        ghostDistance = 1.0/(1.0 + (ghostDistance/(len(GhostStatesList))))
        
        #set the initial cap distance to positive max
        capDist = float('inf')
        #parsing through the cap states in all the current capsules
        for presentCapsuleState in CapsulesStatesList:
            #evaluating the manhattan distance between pacman's current position and capsule state
            #comparing it with the capsule distance and storing the minimum of them
            capDist = min(capDist,manhattanDistance(presentPacPos,presentCapsuleState))
        #evaluating the inverse of current capsules based on the lens of current
        #capsules and storing it 
        capDist = 1.0/(1.0 + len(CapsulesStatesList))
        
        #finally returning the best evaluated value based on
        #score,left food, dist from ghost, dist from capsule
        return presentGameScore + (foodParticleLeft + ghostDistance + capDist)
    
    #util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

