torch.manual_seed(1) # reproducibility

####  Define the network parameters:
hiddenSize = 2 # network size, this can be any number (depending on your task)
numClass = 4 # this is the same as our vocab_size

#### Weight matrices for our inputs 
Wz = torch.randn(vocab_size, hiddenSize)
Wr = torch.randn(vocab_size, hiddenSize)
Wh = torch.randn(vocab_size, hiddenSize)

## Intialize the hidden state
# this is for demonstration purposes only, in the actual model it will be initiated during training a loop over the 
# the number of bacthes and updated before passing to the next GRU cell.
h_t_demo = torch.zeros(batch_size, hiddenSize) 

#### Weight matrices for our hidden layer
Uz = torch.randn(hiddenSize, hiddenSize)
Ur = torch.randn(hiddenSize, hiddenSize)
Uh = torch.randn(hiddenSize, hiddenSize)

#### bias vectors for our hidden layer
bz = torch.zeros(hiddenSize)
br = torch.zeros(hiddenSize)
bh = torch.zeros(hiddenSize)

#### Output weights
Wy = torch.randn(hiddenSize, numClass)
by = torch.zeros(numClass)