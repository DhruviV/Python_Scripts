
import pandas as pd

with open("titanic_data.csv") as f:
    with open("copy.txt", "w") as f1:
        for line in f:
            f1.write(line)

df=pd.read_csv('titanic_data.csv')
columns=df.columns.tolist()
columns=columns[::-1]
df=df[columns]
df.to_csv("new_output.csv",index=False,encoding='utf8')

with open("new_output.csv") as f:
    with open("reverse.txt","w")as f1:
        for line in f:
            f1.write(line)