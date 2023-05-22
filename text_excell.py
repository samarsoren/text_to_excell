import pandas as pd
import numpy as np
with open('/content/example.txt',encoding="utf-8") as f:
    contents = f.read()
arr = []
for each in contents.split('.' or '?' ):
    each = each+'.'
    arr.append(each)
sDF = pd.DataFrame({'sentences':arr})
print(sDF)
sDF.to_excel('example.xlsx')
