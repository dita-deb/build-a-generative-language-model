# Import necessary libraries
import os         # For interacting with the operating system
import numpy       # For numerical operations
import pickle      # For loading serialized Python objects
from numpy import dot   # Function to compute dot product of two arrays
from numpy.linalg import norm  # Function to compute the norm (magnitude) of vectors

# Get the absolute path of the current directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the pre-trained word-to-vector mappings from a pickle file
with open(CURRENT_DIR + "/word_to_vector_trsf.pkl", "rb") as pk:
    word_to_vector = pickle.load(pk)

# Function to compute cosine similarity between two vectors
def cosine_similarity(vec_a, vec_b):
    # Calculate the numerator: sum of element-wise product of two vectors
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    # Calculate the denominator: product of the magnitudes of the two vectors
    denominator = (norm(vec_a) * norm(vec_b))
    # Return the cosine similarity value
    return numerator / denominator

# Print cosine similarity between word vectors for specific word pairs
print(cosine_similarity(word_to_vector["plant"], word_to_vector["grow"]))
print(cosine_similarity(word_to_vector["minute"], word_to_vector["plant"]))
print(cosine_similarity(word_to_vector["plant"], word_to_vector["tree"]))
