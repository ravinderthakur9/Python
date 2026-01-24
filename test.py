import pandas as pd

def open_and_show():
    global df
    df = pd.read_excel(r"C:\Users\Ravin\OneDrive\Documents\vanity.xlsx")
    # total_rows =  len(df["Domain"])
    # print(total_rows)
    # blank = pd.isna(df.iloc[0]["Domain"])
    # print(df)
    messages = [] 

    for index,row in df.iterrows():
        # domain = str(row["Domain"]).strip().lower()
        # usergroup = str(row["UserGroup"]).strip().lower()
        # landingpage = str(row["LandingURL"]).strip().lower()
        # redirect_type = int(row["RedirectionType"])
        
        domain_blank = pd.isna(df.iloc[index]["Domain"])
        usergroup_blank = pd.isna(df.iloc[index]["UserGroup"])
        landingpage_blank = pd.isna(df.iloc[index]["LandingUrl"])
        redirect_type_blank = pd.isna(df.iloc[index]["RedirectionType"])
        print(domain_blank)
        
        if domain_blank:
            messages.append(f"Row {index}: ❌ Domain is blank.)")
        else:
            messages.append(f"Row {index}: ✅ Domain is OK")

        if usergroup_blank:
            messages.append(f"Row {index}: ❌ UserGroup is blank.)")
        else:
            messages.append(f"Row {index}: ✅ UserGroup is OK")
            
        if landingpage_blank:
            messages.append(f"Row {index}: ❌ landingpage is blank.)")
        else:
            messages.append(f"Row {index}: ✅ landingpage is OK")

        if redirect_type_blank:
            messages.append(f"Row {index}: ❌ Redirect Type is blank.")
        else:
            messages.append(f"Row {index}: ✅ Redirect Type is OK")
        
    print(messages)
        
open_and_show()