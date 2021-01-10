import os
import pandas as pd

Path = f"C:\\Users\\mayank\\Downloads\\internship-data\\"
ParentDirectory= "ComCrawlData"
Directories = ["HTML", "Merged File", "Text", "TimeTaken", "URL"]
InnerFolder = Path + ParentDirectory

if __name__ == '__main__':
    os.chdir(Path)
    os.mkdir(ParentDirectory)
    Path = Path + ParentDirectory
    os.chdir(Path)
    for i in range(0, len(Directories)):
        os.mkdir(Directories[i])


df = pd.read_excel (r'C:\Users\mayank\Downloads\webinfo.xls')
