import pandas as pd
import numpy as np
import os
import openpyxl
from urlfetcher import df, fname

cwd = os.path.abspath(f'{fname}\\Text\\')
files = os.listdir(cwd)
print(files)


df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        file_path=cwd + '\\' + file
        print(file_path)
        df = df.append(pd.read_excel(file_path, engine='openpyxl'))
df.to_excel(f'{fname}\\MergedFile\\merged.xlsx')