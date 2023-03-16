# There are a few ways for a misspelling.
# Substitution, where a letter is replaced with the wrong one.
# Switching, where two letters are switched.
# Deletion, where one or more letters are missed.

# This can be handled with the following module
from autocorrect import Speller

check = Speller()
Unclean = open("Input.txt", "r")
Query = Unclean.readline().strip()
Cleaned = check(Query)
print(Cleaned)
Writer = open("Cleaned.txt","w")
Writer.write(Cleaned)
