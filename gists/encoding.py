character_list = list(set(text))   # get all of the unique letters in our text variable
vocabulary_size = len(character_list)   # count the number of unique elements
character_dictionary = {'h': 0, 'a': 1, 't': 2, 'M': 3}
# {char:e for e, char in enumerate(character_list)}  # create a dictionary mapping each unique char to a number
encoded_chars = [character_dictionary[char] for char in text] #integer representation of our vocabulary 