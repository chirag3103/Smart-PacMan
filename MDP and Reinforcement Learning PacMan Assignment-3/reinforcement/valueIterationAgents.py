# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        #U_dict = util.Counter()
        #delta = 0

        for i in range(0,self.iterations):
            #initialized the dictionary
            U_dict = util.Counter()
            #parsing all the states of MDP
            for present_State in mdp.getStates():
                #checked for the terminal state
                if mdp.isTerminal(present_State):
                    #if it is the terminal state then exit the loop
                    U_dict[present_State] = 0
                    continue;
                #if not a terminal state then, looking for
                #possible legal actions
                legal_Actions = mdp.getPossibleActions(present_State)
                #if no possible actions then return 0
                if not legal_Actions:
                    U_dict[present_State] = 0
                #setting a max as negative max
                maxqValue = float('-inf')
                #set initial qValue to zero
                qValue = 0
                #parsing all the actions 
                for present_Action in legal_Actions:
                    #setting the qvalue as a 2-item tuple
                    #of state and action
                    qValue = self.getQValue(present_State,present_Action);
                    
                    #checking for the greater qvalue
                    if qValue > maxqValue:
                        #if greater then exchanging values
                        maxqValue = qValue
                        #storing the qvalue to the dict
                        U_dict[present_State] = qValue
            self.values = U_dict
        

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        qValue = 0
        #parsing through the state problem pair to compute the
        #qvalue from values
        for present_State, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            qValue += prob * (self.mdp.getReward(state,action,present_State) + self.discount*self.getValue(present_State))

        return qValue
        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        bestAction = None
        maxqValue = float('-inf')
        #getting the possible actions of the given state
        legal_Actions = self.mdp.getPossibleActions(state)
        #if no legal actions then return zero
        if not legal_Actions:
            return None
        qValue = 0
        #parsing through all the legal actions
        for present_Action in legal_Actions:
            #get the Qvalue of the current state and action pair
            qValue = self.getQValue(state,present_Action);
            #compare if the value is greater than max
            if qValue >= maxqValue:
                #if yes then exchanging values and setting
                #bestAction as the present action
                bestAction = present_Action
                maxqValue = qValue

        return bestAction
        
        
        
        
        
        
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
