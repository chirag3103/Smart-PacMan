README.txt
Name: Chirag Madhukar Agarwal
SFID: 918292042

multiAgents.py:
The reflex agent was pretty straight forward. But that was because it was clearly mentioned that, make use of both food and ghost locations.

I had understood the logic and working of the minimax agent during the lecture. Due to which it did not involve much complexity for me.
Just that the minimizers were the ghosts moves and maximizer was the pacman's move.

I took the most time in the third and the fifth question.
Third being the alpha beta pruning. 
Even though the implementation as a flowchart was provided, it still took me time to get it converted into an equivalent code.

And the fifth being the evaluationn function. 
I did not know about the capsule states and values due to which i took extra time to figure this one out.
Here the main hint was to use the reciprocal of the important values obtained from the reflex agent. What took the most time for me was the values which i need to combine in order to return from the evaluaion function.
Then finally i made a perfect combination of score with a set of foodleft;ghostdist;capsuledist.

The fourth was the Expectimax. This was my favorite part of the assignment. I followed the instructions given in the assignment guide.
And also followed the psedocode of the lecture. Made use of float for the averages. This made the first part of the question easy. Later came the peculiar part.
Where the pacman was never left alone by the ghosts.
I was happy to see that my Expectimax agent atleast won......rather than the Alpha-beta agent, which kept loosing every now and then.


Hours spent doing this assignment: 
I had started assignment 2 on the 29th of September. And I finished it last evening. I dedicated 2-4hours a day. Hence the total number of hours I spent comes out to be, 30-34hrs.
 
Thank you.
