# h gets updated and then we calculate for the next 
h_t_1 = []
h = h_t_demo
for i,sequence in enumerate(X[0]):   # iterate over each sequence in the batch to calculate the hidden state h 
    z = torch.sigmoid(torch.matmul(sequence, Wz) + torch.matmul(h, Uz) + bz)
    r = torch.sigmoid(torch.matmul(sequence, Wr) + torch.matmul(h, Ur) + br)
    h_tilde = torch.tanh(torch.matmul(sequence, Wh) + torch.matmul(r * h, Uh) + bh)
    h = z * h + (1 - z) * h_tilde
    h_t_1.append(h)
    print(f'h{i}:{h}')
h_t_1 = torch.stack(h_t_1)