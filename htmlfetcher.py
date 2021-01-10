from comcrawl import IndexClient
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor

from urlfetcher import df, fname

'''
websites = ["asmag", "AmericanMachinist", "assemblymag", "automationworld"]

# [ "aviationweek", "BestManufacturingPractices", "Chemengonline","ComputerWeekly", "Cordis.europ", "den" ]
'''


def fetch(website, filter, filtertype):

    start = time.time()
    client = IndexClient()

    dataframe = pd.read_csv(f"{fname}\\url\\{website}.csv")
    print(len(dataframe))
    print(len(df))
    dataframe["url"] = dataframe["url"].str.lower()
    my_list = filter.split(",")
    # all the filter parameter

    if filtertype=='notrequired':
        filter = dataframe[~dataframe['url'].str.contains('|'.join(my_list))]

    elif filtertype=='required':
        filter = dataframe[dataframe['url'].str.contains('|'.join(my_list))]

    else:
        filter = dataframe

    print("after filter", len(filter))
    try:
        client.results = filter.to_dict("records")
        client.download(threads=4)
        htmldf = pd.DataFrame(client.results)
    except:
        return("empty")
    end = time.time()
    timetaken=end-start
    with open(f'{fname}\\timetaken\\{website}CCtime.txt', 'w') as f:
        f.write( f"time taken is {timetaken}")

    return(htmldf)



def html_collector(df):
    print("main")

    with ThreadPoolExecutor(max_workers=10) as executor:  # using ThreadPoolExecutor with number of threads.
        x = executor.map(fetch, df['foldername'], df['filters'], df['filtertype'])   # mapping function fetch with session 100times and 100 urls
        executor.shutdown(wait=True)  # wait everything until x fetches every data
    print("batch completed")
    return(list(x))









temp = html_collector(df)
for j in range(0, len(temp)):
    temp1= pd.DataFrame(temp[j])
    temp1.to_json(f"{fname}\\html\\{df['foldername'][j]}urldHTML.gz", compression="gzip")

print("file created")



