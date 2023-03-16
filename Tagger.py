# Given an input in Cleaned.txt, this code tags each word as a verb, pronoun, or some other type, as well as
# breaking it up.
import nltk as nk

Unprocessed = open("Cleaned.txt", "r")
Query = Unprocessed.readline()



tokens = nk.word_tokenize(Query)
print(tokens)
# TODO: Optimize these two lines by not needing to download this again every time
nk.download('maxent_ne_chunker')
nk.download('words')
tagged = nk.pos_tag(tokens)
print(tagged)
