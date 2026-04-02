Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> df = pd.read_csv("C:\Users\KUSHAL\Downloads\experience.csv")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> df = pd.read_csv("C:/Users/KUSHAL/Downloads/experience.csv")
>>> print("Full DataFrame:")
Full DataFrame:
>>> print(df)
     name  yrs
0  kushal    7
1  ricchy    9
2   honey   20
>>> rows, columns = df.shape
>>> print("\nNumber of rows:", rows)

Number of rows: 3
>>> KeyboardInterrupt
>>> print("Number of columns:", columns)
Number of columns: 2
>>> print("\nLength of DataFrame:", len(df))

Length of DataFrame: 3
>>> print("\nFirst 2 rows:")

First 2 rows:
>>> 
>>> print(df.head(2))
     name  yrs
0  kushal    7
1  ricchy    9
