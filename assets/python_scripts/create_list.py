import subprocess
import sys
import pandas as pd
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

query_str = ['./fasttext', 'multiple', 'result/clean_recipe.bin']
argv_len = len(sys.argv)
if argv_len == 1:
    print('Please insert one or many ingredients, try again!')
    sys.exit()
for i in range(argv_len):
    query_str.append(sys.argv[i])

print(query_str)

finish_str = subprocess.check_output(query_str)
finish_str = finish_str.decode('UTF-8')
list_data = StringIO(finish_str)
df = pd.read_csv(list_data, sep=" ",header=None)
print(df)
