import pandas as pd
from urlfetcher import fname

file_path= f'{fname}\\MergedFile\\merged.xlsx'

file=pd.read_excel(file_path, engine='openpyxl')

df= file[file['text'].notna()]



df= df.drop_duplicates(subset='text', keep='first')

#df.to_csv(f'{fname}\\MergedFile\\aftercleaning.gz', compression='gzip')
#df.to_json(f'{fname}\\MergedFile\\aftercleaning.json')

df.to_excel(f'{fname}\\MergedFile\\aftercleaning.xlsx')