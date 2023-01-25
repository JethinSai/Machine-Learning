Given = "I am a teacher and I love to inspire and teach people"
# Here we are going to split the given sentence usings split funtion
words = Given.split()
# To find the unique words we are converting words list into set
unique_words = set(words) # In Set no same words are repeated so remining are unique_words
# Print the number of unique words
print("The number of unique words used in the sentence is .",len(unique_words))
