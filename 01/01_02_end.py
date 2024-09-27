import random                           # Import the random module to enable random selection of items.
from collections import defaultdict     # Import defaultdict to create a dictionary with default values.

# List of tokens (words) to be used in the program.
tokens = ["I", "try", "to", "learn", "something", "new", "every", "day"]

# Create a defaultdict with lists as default values for storing graph connections.
graph = defaultdict(list)

# Print the default value for a key that doesn't exist in the graph dictionary.
# This will output an empty list since "word" has not been added to the graph.
print(graph["word"])

# Enumerate through the tokens list, providing both the index (i) and the token value.
for i, token in enumerate(tokens):
    print(i, token)             # Print the index and the corresponding token.

# Randomly select and print a token from the tokens list three times.
print(random.choice(tokens))            # Print a random token from the tokens list.
print(random.choice(tokens))            # Print another random token from the tokens list.
print(random.choice(tokens))            # Print yet another random token from the tokens list.
