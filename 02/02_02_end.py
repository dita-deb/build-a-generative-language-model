from string import punctuation                          # Import punctuation for text processing
from collections import Counter, defaultdict              # Import collections for counting occurrences

# Sample dataset: A list of tuples where each tuple contains a comment (text) and its sentiment label ('pos' for positive and 'neg' for negative)
post_comments_with_labels = [
    ("I love this post.", "pos"),                       # Positive comment
    ("This post is your best work.", "pos"),            # Positive comment
    ("I really liked this post.", "pos"),               # Positive comment
    ('I agree 100 percent. This is true', 'pos'),       # Positive comment
    ("This post is spot on!", "pos"),                   # Positive comment
    ("So smart!", "pos"),                               # Positive comment
    ("What a good point!", "pos"),                      # Positive comment
    ("Bad stuff.", "neg"),                              # Negative comment
    ("I hate this.", "neg"),                            # Negative comment
    ("This post is horrible.", "neg"),                  # Negative comment
    ("I really disliked this post.", "neg"),            # Negative comment
    ("What a waste of time.", "neg"),                   # Negative comment
    ("I do not agree with this post.", "neg"),          # Negative comment
    ("I can't believe you would post this.", "neg"),    # Negative comment
]

class NaiveBayesClassifier:
    def __init__(self, samples):                         # Initialize the classifier with a dataset of samples
        self.mapping = {"pos": [], "neg": []}            # Mapping to store tokenized words for positive and negative labels
        self.sample_count = len(samples)                 # Total number of samples in the dataset
        
        # Tokenize the text from each sample and group them by their respective label (pos/neg)
        for text, label in samples:                       # Iterate over each sample
            self.mapping[label] += self.tokenize(text)   # Tokenize and map to corresponding label
        
        # Count the occurrence of each token in positive and negative labeled data
        self.pos_counter = Counter(self.mapping["pos"])   # Counter for positive tokens
        self.neg_counter = Counter(self.mapping["neg"])   # Counter for negative tokens

    @staticmethod
    def tokenize(text):                                   # Convert text to lowercase, remove punctuation and numbers, and split into tokens (words)
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))  # Remove punctuation and numbers
            .replace("\n", " ")                            # Replace newline characters with spaces
            .split(" ")                                   # Split the text into individual words
        )

    def classify(self, text):                             # Tokenize the input text to classify its sentiment
        tokens = self.tokenize(text)                       # Tokenize the input text
        
        # Initialize probabilities for positive and negative classes
        pos_prob = 0                                       # Cumulative probability for positive sentiment
        neg_prob = 0                                       # Cumulative probability for negative sentiment

        # Calculate probabilities for each token's presence in positive and negative samples
        for token in tokens:                               # Iterate over each token
            # Calculate the probability of the token being in the positive samples
            pos_token_prob = self.pos_counter[token] / self.sample_count  # Probability of token in positive class
            neg_token_prob = self.neg_counter[token] / self.sample_count  # Probability of token in negative class
            
            # Accumulate probabilities for classification
            pos_prob += pos_token_prob                      # Add to positive probability
            neg_prob += neg_token_prob                      # Add to negative probability
        
        # Classify based on the total probabilities calculated
        if pos_prob > neg_prob:                           # Check if positive probability is higher
            return "pos"                                   # Return 'pos' if positive probability is higher
        elif neg_prob > pos_prob:                         # Check if negative probability is higher
            return "neg"                                   # Return 'neg' if negative probability is higher
        else:                                             # Handle case where probabilities are equal
            return "neutral"                               # Return 'neutral'

# Create an instance of the NaiveBayesClassifier with the given post comments and labels
cl = NaiveBayesClassifier(post_comments_with_labels)     # Initialize classifier with sample data

# Flags for showing expected results and hints (for testing purposes)
show_expected_result = False                              # Placeholder flag for expected results
show_hints = False                                        # Placeholder flag for hints

def get_sentiment(text):                                  # Use the classifier to classify the input text
    return cl.classify(text)                              # Return the classification result

# # Example usage
# if __name__ == "__main__":                               # Entry point for the script
#     text = "I love this post."                           # Input text for sentiment analysis
#     result = get_sentiment(text)                         # Get the sentiment of the input text
#     print(result)                                        # Print the expected output: "pos"
