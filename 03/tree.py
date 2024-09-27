import numpy as np

# Define extended word vectors to include all the necessary words
word_to_vector = {
    "tree": np.array([1.0, 0.0, 0.0]),  # Reference vector for "tree"
    "wood": np.array([0.9, 0.1, 0.0]),  # Similar to "tree"
    "plant": np.array([0.8, 0.2, 0.0]),  # Similar to "tree"
    "saw": np.array([0.7, 0.3, 0.0]),   # Some similarity to "tree"
    "farm": np.array([0.6, 0.4, 0.0]),  # Some similarity to "tree"
    "base": np.array([0.5, 0.5, 0.0]),  # Some similarity to "tree"
    "star": np.array([0.4, 0.6, 0.0]),  # Less similar
    "door": np.array([0.3, 0.7, 0.0]),  # Less similar
    "bird": np.array([0.2, 0.8, 0.0]),  # Less similar
    "grow": np.array([0.1, 0.9, 0.0]),  # Less similar
}

def cosine_similarity(vec_a, vec_b):
    """Calculate the cosine similarity between two vectors."""
    numerator = np.dot(vec_a, vec_b)  # Dot product of the vectors
    denominator = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)  # Product of the norms
    return numerator / denominator if denominator != 0 else 0.0  # Handle zero division

def similar_words(word="tree", top_k=10):
    """Find the top K most similar words to the given word."""
    if word not in word_to_vector:
        return []  # Return empty if the word isn't found

    word_vector = word_to_vector[word]  # Get the vector of the input word
    similarities = []  # List to store similarities

    # Calculate cosine similarity for each candidate word
    for candidate_word, vector in word_to_vector.items():
        if candidate_word != word:  # Skip the input word itself
            sim = cosine_similarity(word_vector, vector)  # Calculate similarity
            similarities.append((candidate_word, sim))  # Store word and its similarity

    # Sort by similarity (highest first) and get the top K similar words
    similar_words = sorted(similarities, key=lambda x: -x[1])[:top_k]

    # Return the most similar words including the original word
    return [word] + [word for word, _ in similar_words]  # Return original word and similar words