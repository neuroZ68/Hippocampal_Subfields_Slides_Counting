import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
df = df.append([2, 3])
print(df)
