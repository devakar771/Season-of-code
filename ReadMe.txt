game2048_engine: The core engine of the game that allows the user or a model to interact with the game.
model: 		 The architecture of the neural network is defined using keras.
Game2048: 	 The GUI for the game will allows the user to see the outcomes using graphical elements. 
	  	 Implemented using tkinter.

For learning the Q-values a convolution network was used. Can be viewed from "Architecture.png".
Constants used:
# board_size = 4
# gamma for Q-learning: 0.9
# capacity of memory after which the the saved experiences are used to train the NN: 6144
# batch size of the saved experiences used training: 512
# coefficient of reward given for getting max value: 0.1

# initial learning rate: 0.001 --> exponential decay
# initial epsilon for epsilon greedy approach: 0.9 --> epsilon /= 1.005 after episodes > 20000
# if random number < epsilon then a move is sampled from the q-values output from the NN not by assuming 
  a uniform distribution but instead the output was sent to a softmax layer to extract the probabilties and 
  then sample a move considering the probabilities. 

# Loss function: Meaen squared error
# Optimizer: 	 RMS prop

# Final trainied weights: bestWt.zip
