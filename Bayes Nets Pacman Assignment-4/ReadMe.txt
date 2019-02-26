README.txt
Name: Chirag Madhukar Agarwal
SFID: 918292042

factorOperations.py:
inference.py:
bayesAgents.py:

The hints mentioned before every snippet in the code helped alot. Because was tough to understand where to exactly start from.
question1:
constructBayesNet in bayesAgents.py
successfully created an empty bayes net.
Obtained the full set of observations as guided in the sample code.
added the observations to the array for every house and observed positions.
initialized the dictionary at every observed value to an empty constant.
populated the food and ghost edges.

question2:
fillYCPT and fillObsCPT in bayesAgents.py
At first i could not figure out which observation variables to consider. After reading the hint at least one thing was clear that there needed to be four variables. Then i figured out that i need to consider both top and bottom along with left top and bottom, as we are talking about the y axis variable.
Obtained the full set of observations by the same method. For each observed CPT, stored the ghost and food house value. Stored the color of the current observation, and the block details. After checking the block for ghost or food house, set the probability with the observation and CPT. Set the CPT in the bayes network in the end.

question3:
joinFactors in factorOperations.py
checked for non empty factors
parsed through all the factors and calculated the unconditional and conditional variables
set the probability of each assignment in the newFactor

question4:
eliminate in factorOperations.py
took a conditional and unconditional factor. took the variable dict and passed the elimination var. got rid of the elimination var and returned a new factor without the elimination variable.

question5:
normalize in factorOperations.py 
take all the factor as input normalize them, scale the entries such that their sum in the factor is 1


question6:
inferenceByVariableElimination function in inference.py
checking all the factors. if the len of any factor is > 1 eliminating that var and adding a new factor to the list
finally appending the list of factors and normalizing it before returning.

quesion7:
inferenceByVariableElimination in bayesAgents.py
initially i wrote an around the corner method for this function and moved on with the remaining questions. But later i managed to modify certain statements as i was just repeating the lines of code unncessarily.
hence, this function now evaluates the best good house position.

question8:
computeEnterValues and computeExploreValue in bayesAgents
tried to compute the value of entering the left and right houses as adviced in the code. Made use of Reward vars to better understand the reward of entering each house.
computed the expected value of entering left or right houses


Hours spent doing this assignment: 
I had started assignment 4 on the 20th of November. And I finished it last night. I dedicated 2-3hours a day. Hence the total number of hours I spent comes out to be, 20-30hrs.

Thank you.
