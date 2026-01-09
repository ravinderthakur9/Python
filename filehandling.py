import pandas as pd

def fileopen():
    df = pd.read_excel("Test.xlsx")
    return df

fileopen()
