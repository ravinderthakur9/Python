import pandas as pd

def validate_data():
    df = pd.read_excel(r"C:\Users\Shiv_Ravinder_Singh\OneDrive - Dell Technologies\Desktop\validatedata.xlsx")
    print(df["Domain"][0])
    total = len(df["UserGroup"])
    for i in range(total):
        print(df["Domain"][i])
    
    
validate_data()