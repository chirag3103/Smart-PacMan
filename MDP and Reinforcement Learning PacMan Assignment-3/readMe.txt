SFID: 918292042

Question 1: Implemented the ValueIterationAgent in valueIterationAgents.py
iterated over all the states in mdp to check if they are terminal states or not. if yes then dict saves a zero for that state. else parsed over all the possibe legal actions of that state. for every legal action, checked the current action. calculated the qvalue for the current state and action pair. recursively checking for the max qvalue and storing the qvalue state pair in the dict.

Question 2: changed the discount parameter and left the noise parameter as it is in question2() of analysis.py

Question 3: choose a differnt setting of discount, noise and living reward parameters of MDP for question3a() through question3e() in analysis.py
tried and tested various combination of 3-tuples and came up with the assigned value combo's

Question 4: implemented the update,computeValueFromQValue and computeActionFromQValues methods of QLearningAgent in qlearningAgents.py. where update,computeValueFromQValue and computeActionFromQValues were pretty easy for me. But the update() took a bit of extra time, as getting all the parameters right was tough.

Question 5: implemented the getAction() in qlearningAgents.py. Made use of the util.flipCoin() and random.choice() for selecting anyone of the legal actions available as per the assignment sheet.

Question 6: after training the Qlearner on noiseless BridgeGrid for 50 episodes question6() in analysis.py returned a 'NOT POSSIBLE'. as there are no epsilon and learning rate for which the policy learnt
  
Question 7: As per the assignment sheet a PacmanQAgent is already defined as QLearningAgent which i implemented in question 4 and 5. just the learning parameters are different for the pacman.

Question 8: implemented the ApproximateQAgent in qlearningAgents.py wrote the getQValue() and update()

Hours spent doing this assignment: 
I had started assignment 2 on the 30th of October. And I finished it late last night. I dedicated about 3hours every day. Hence the total number of hours I spent comes out to be, 30-34hrs.
 
This assignment was a bit more challenging than the others but i enjoyed completing all questions.

Thank you.

