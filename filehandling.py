import pandas as pd

def fileopen():
    df = pd.read_excel(r"C:\Users\Shiv_Ravinder_Singh\OneDrive - Dell Technologies\Documents\Python\Test.xlsx")
    return df

fileopen()
