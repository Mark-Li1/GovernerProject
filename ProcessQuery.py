import Preprocessing as prp
import pandas as pd

enter = open("Input.txt", "r")
prp.enterQuery(enter.readline())
enter.close()

df = prp.start()
print(df)

