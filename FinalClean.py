# This code fixes contractions, such as "cant" -> "can't, and then runs the fixed string through the tagger again.
# This can be cycled a few times to increase chances of working,  alongside the tagger.

import pandas as pd

df = pd.read_csv("Tagged.csv")
print(df.shape)
length = df.shape[0]
build = ""
for i in range(2, length):
    wordType = str(df.loc[i][1])
    word = str(df.loc[i][0]).lower().strip()
    print(wordType + ": " + word)
    concat = ""
    if word.__eq__("cant") & (wordType.__eq__("VBP")):
        concat = "can not "
    elif word.__eq__("wont"):
        concat = "will not "
    elif word.__eq__("shouldnt"):
        concat = "should not "
    elif word.__eq__("dont"):
        concat = "do not "
    else:
        build = build + word + " "
    build = build + concat


build: str = build.strip()
print(build)
