import re

# OR (found online)
def letter_histogram(word):
    histogram = dict()
    for letter in word:
        histogram[letter] = histogram.get(letter, 0) + 1
    return histogram

print(letter_histogram("banana"))

# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')
def word_histogram(sentence):
    histogram = dict()
    for word in re.split(r"\s+|\,\s+|\,|--", sentence):
        word = word.lower()
        if word in stop_words:
            continue
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram

def sort_histogram_by_value(histogram):
    return sorted(histogram.items(), 
                  key=lambda k_v_pair: k_v_pair[1], 
                  reverse=True)

with open("declaration_of_independence.txt", "r") as file:
    declaration = file.read()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
# print(declaration)
print(sort_histogram_by_value(word_histogram(declaration))[:10])
