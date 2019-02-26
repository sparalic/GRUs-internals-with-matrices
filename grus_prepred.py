def one_hot_encode(encoded, vocab_size):
    result = torch.zeros((len(encoded), vocab_size))
    for i, idx in enumerate(encoded):
        result[i, idx] = 1.0
    return result


# One hot encode our encoded charactes
batch_size = 2
seq_length = 3
num_samples = (len(encoded_chars) - 1) // seq_length # time lag of 1 for creating the labels
vocab_size = 4

data = one_hot_encode(encoded_chars[:seq_length*num_samples], vocab_size).reshape((num_samples, seq_length, vocab_size))
num_batches = len(data) // batch_size
X = data[:num_batches*batch_size].reshape((num_batches, batch_size, seq_length, vocab_size))
# swap batch_size and seq_length axis to make later access easier
X = X.transpose(1, 2)

# +1 shift the labels by one so that given the previous letter the char we should predict would be or next char
labels = one_hot_encode(encoded_chars[1:seq_length*num_samples+1], vocab_size) 
y = labels.reshape((num_batches, batch_size, seq_length, vocab_size))
y = y.transpose(1, 2) # transpose the first and second index
y,y.shape