import random
from string import punctuation
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        # Initialize a graph where each key is a token (word), 
        # and its value is a list of possible next tokens
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        # Tokenize the input text by removing punctuation and numbers,
        # replacing new lines with spaces, and splitting the text into words
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        # Tokenize the text into a list of words (tokens)
        tokens = self._tokenize(text)
        # Build the graph by mapping each token to its next token in the text
        for i, token in enumerate(tokens):
            # Stop if we reach the last token, as there is no next token
            if (len(tokens) - 1) == i:
                break
            # Add the next token to the list of possible next tokens for the current token
            self.graph[token].append(tokens[i + 1])

    def generate(self, prompt, length=10):
        # Get the last word from the prompt, which will be the starting point
        current = self._tokenize(prompt)[-1]
        # Initialize the output with the provided prompt
        output = prompt
        # Generate a sequence of tokens
        for i in range(length):
            # Retrieve possible next words (tokens) for the current word from the graph
            options = self.graph.get(current, [])
            # If there are no next options, stop the generation
            if not options:
                break
            # Randomly choose the next word from the available options
            current = random.choice(options)
            # Add the chosen word to the output string
            output += " " + current
        return output
