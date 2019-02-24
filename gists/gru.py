def gru(x, h):
    ht_2 = [] # stores the calculated h for each input x
    outputs = []
    h = torch.zeros(batch_size, hiddenSize) # intitalizes the hidden state
    for i in range(num_batches):  # this loops over the batches 
        x = X[i]
        for i,sequence in enumerate(x): # iterates over the sequences in each batch
            z = torch.sigmoid(torch.matmul(sequence, Wz) + torch.matmul(h, Uz) + bz)
            r = torch.sigmoid(torch.matmul(sequence, Wr) + torch.matmul(h, Ur) + br)
            h_tilde = torch.tanh(torch.matmul(sequence, Wh) + torch.matmul(r * h, Uh) + bh)
            h = z * h + (1 - z) * h_tilde

            # Linear layer
            y_linear = torch.matmul(h, Wy) + by

            # Softmax activation function
            y_t = F.softmax(y_linear, dim=1)

            ht_2.append(h)
            outputs.append(y_t)
        return torch.stack(outputs), torch.stack(ht_2)
    