import pickle  # Import the pickle module for loading serialized Python objects

# Load the word vectors from a pickle file
with open("./deps/deps/word_to_vector_trsf.pkl", "rb") as pk:
    word_to_vector = pickle.load(pk)  # Deserialize the word vectors into a dictionary

def cosine_similarity(vec_a, vec_b):
    """Calculate the cosine similarity between two vectors."""
    # Compute the dot product of the two vectors
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])  # Dot product

    # Calculate the magnitude (norm) of each vector
    denominator = (sum([vec_a[i] ** 2 for i in range(len(vec_a))]) ** 0.5 * 
                   sum([vec_b[i] ** 2 for i in range(len(vec_b))]) ** 0.5)  # Magnitude

    # Return the cosine similarity; handle division by zero to avoid errors
    return numerator / denominator if denominator != 0 else 0.0  # Handle division by zero

def similar_words(word="tree", top_k=10):
    """Find the top K most similar words to the given word."""
    if word not in word_to_vector:
        return []  # Return an empty list if the word isn't found in the vector dictionary

    word_vector = word_to_vector[word]  # Retrieve the vector corresponding to the input word

    # Sort the candidate words by their cosine similarity to the input word's vector
    sorted_words = sorted(
        word_to_vector.keys(),
        key=lambda x: cosine_similarity(word_to_vector[x], word_vector),  # Calculate similarity
        reverse=True  # Sort in descending order (most similar first)
    )

    return sorted_words[:top_k]  # Return the top K most similar words
