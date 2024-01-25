# Given a string of words, create a set of every sequential bi-gram.  Bigrams are two-word combinations of the text, i.e. “Charlie rocks”.
 
# Example
# "Make a killer impression on whoever you’re meeting."
 
# returns
# “Make a"
# “a killer"
# “killer impression"
# “impression on"
# Etc.

# requirements
# Generates a set of every possible bigram from a string of text
# Keep performance & memory usage in mind
# Include tests
# We prefer Ruby or Python, but you may use any language.


# split_sentence = sentence.split(" ")
# num = 2
# bi_gram = split_sentence[:2]
# bi_gram = " ".join(bi_gram)
# print(bi_gram)

sentence = input("Input sentence here: ")

def splitter(sentence): 
  x = 0
  i = 2
  split_sentence = sentence.split(" ")
  while i < len(split_sentence):
    bi_gram = ""
    split_array = (split_sentence[x:i])
    bi_gram = " ".join(split_array)
    print(bi_gram)
    i += 2
    x += 2

splitter(sentence)



  

