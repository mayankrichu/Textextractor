import pandas as pd
from urlfetcher import fname
import time
start=time.time()
file_path= f'{fname}\\MergedFile\\aftercleaning.json'

file=pd.read_json(file_path)

print(file.info())

file1=file.drop(file.columns[[0,1]], axis = 1)

file1.to_excel(f'{fname}\\MergedFile\\aftercleaning1.xlsx')

end=time.time()

print(f'{end-start}')