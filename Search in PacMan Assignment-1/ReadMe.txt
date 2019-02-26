README.txt
Name: Chirag Madhukar Agarwal
SFID: 918292042

Search.py:
The DFS and BFS algorithms were straight forward. They were implemented by following the pseudocodes provided in the slides of the lectures. I just took care about two things: a node which has already been visited once does not get added to the frontier and that after visiting each node, the frontier must be updated not only with that node but also with the actions that need to be performed.
Regarding the UCS algorithm, I took a little more time If compared to the above two. This is because, in UCS I had to take into consideration the cost of visiting each node. Though it was simple as I just had to add the costs, but the idea that I had to define the priority queue in such a way that it stores the tuple of node, action, cost and weight, right from the beginning did not strike soon.
The A star algorithm took the most of my time. Actually A star algorithm did not have any much change from the UCS apart from considering the heuristic value. After reading from the AI textbook, I realised that if I supply the state and problem to the heuristic function it will return me the hvalue which then just needs to be added.

SearchAgents.py
The 5th question was simple, but the condition was that it uses the BFS algorithm to find the corners, hence I could not do it earlier. And another thing that I need a proper identification mechanism of the corner points.
The 6th question was and still remains the tricky one, as I was not able to get a effective heuristic model for the corners. Even though I am getting the solution, the number of nodes visited are 1966. Because of this I am getting a zero in that question. Hence, I request you to consider my efforts too.
The 7th question, I just made use of the conditions which are required to find out the location of the food particles and pacman. And then calculating the distance between them and helping the pacman to reach the non-eaten food particles. Though I completed it, I got a 3 on 4 because my expanded nodes are 9551, where as it was supposed to be less than 7000 for a 4.
The 8th was simple just because of the hint given in the assignment pdf. I just had to define the goal test and it was done in no time.

Hours spent doing this assignment: 
I had started assignment 1 on the 15th of September. And I finished it last night. I dedicated 3-4hours a day. Hence the total number of hours I spent comes out to be, 24-28hrs.
 
Before I conclude, I would like to give courtesy to my friend Girish, who helped me with the syntax of data structures of python. As this was one of my biggest achievements in python, I had trouble in various places where I did not know how to figure out the syntax of an expression. In such situations I made use of the internet and Girish helped me too.

Thank you.
