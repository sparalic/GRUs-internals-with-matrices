def sample(primer, length_chars_predict):
    
    word = primer

    primer_dictionary = [character_dictionary[char] for char in word]
    test_input = one_hot_encode(primer_dictionary, vocab_size)
    

    h = torch.zeros(1, hiddenSize)

    for i in range(length_chars_predict):
        outputs, h = gru(test_input, h)
        choice = np.random.choice(vocab_size, p=outputs[-1][0].numpy())
        word += character_list[choice]
        input_sequence = one_hot_encode([choice],vocab_size)
    return word

max_epochs = 10  # passes through the data
for e in range(max_epochs):
    h = torch.zeros(batch_size, hiddenSize)
    for i in range(num_batches):
        x_in = X[i]
        y_in = y[i]
        
        out, h = gru(x, h)
        print(sample('Ma',20))