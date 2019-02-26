README.txt
Name: Chirag Madhukar Agarwal
SFID: 918292042

The hints mentioned before every snippet in the code helped alot. Because was tough to understand where to exactly start from.
question1:
train() in perceptron.py
started with initialzing the weights of the training data and labels.
parsed through all the legal labels to calculate the scores
compared the labels. updated the weights 

question2:
findHighWeightFeatures() in perceptron.py
initialized a feautre and weight list
parsed through each feature
initialized the label and current feautre
sorted the weights
and returned
answers.py
returned 'a'

question3:
trainAndTune() in mira.py
initialized the training weight list. parsed through all the values in the c grid. copied the weights of the c grid to the training the weight list.
parsed through the training data. classified the training data and labels.
calculate the values using the formula's given in the guidlines doc.
parsed through the training data keys and updated the training weight lists.
parsed through all the c values in the c grid. updated the training weight list.
updated the classified data list. parsed through the classified data. calculated the score and index values and updated weights list.


question4:
EnhancedFeatureExtractorDigit in dataClassifier.py
for the basic features
started with intializing the height and width of the digit datnum.
parsed through the width and height to get the pixel values and setting the feautres to 1/0 accordingly
for the advanced feautures
parsed through the height and width to get the pixel values.
initlialized all the advances features
checked the pixel frequency and returned the features.

question5:
train() in perceptron_pacman.py
stored the current training label for the current data. parsed thorugh all the legal values to calculate the score. initialized the weights for my training data.

question6:
EnhancedPacmanFeatures() in dataClassifier.py
started with generating the successor for the given state and given action. stored the food count,list of capsules, location of the pacman for the next successor state.
sotre the food for the given state. calculated the height and widht of the food particle. calculated the x and y coordinates of the food particle.
used it to calculate the manhattan distance the food particle and the pacman. compared and stored the distance.
parsed through all the ghost states. stored the manhattan distance between the ghost and the pacman.
parsed through all the capsules. stored the manhattan distance between the pacman and the current capsule.
updated the feautres and returned.

Hours spent doing this assignment: 
I had started assignment 5 on the 15th of December. And I finished it today evening. I dedicated 2-3hours a day. Hence the total number of hours I spent comes out to be, 18-25hrs.

Thank you.
