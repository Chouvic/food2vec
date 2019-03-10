import pandas as pd

with open('kaggle_clean.csv') as f:
    lines = f.readlines()

print(lines[1])

df = pd.read_csv('kaggle_clean.csv', sep=' ',header=None)
print(df.head())

print(df.shape)
names = df.ix[:,0]
df_values = df.drop(df.columns[0], axis=1)
df_values = df_values.values
print(df_values[0])
print(names[0])
with open('correct_format.js', "w+") as f:
    for i in range(df.shape[0]):
        if(i == 0):
            f.write("var wordVecs={")
        for j in range(101):
            if(j == 0):
                f.write("\"%s\":["%names[i])
            elif(j == 100):
                f.write("%f], "%df_values[i][j-1])
            else:
                f.write("%f, "%float(df_values[i][j-1]))
        if(i == df.shape[0] -1):
            f.write("};")
