import pandas as pd

def open_and_show():
    global df
    df = pd.read_excel(r"C:\Users\Shiv_Ravinder_Singh\OneDrive - Dell Technologies\Desktop\intake_template_validated.xlsx")
    # total_rows =  len(df["Domain"])
    # print(total_rows)
    # blank = pd.isna(df.iloc[0]["Domain"])
    # print(df)
    
    for index,row in df.iterrows():
        # domain = str(row["Domain"]).strip().lower()
        # usergroup = str(row["UserGroup"]).strip().lower()
        # landingpage = str(row["LandingURL"]).strip().lower()
        # redirect_type = int(row["RedirectionType"])
        messages = []
        domain_blank = pd.isna(df.iloc[index]["Domain"])
        usergroup_blank = pd.isna(df.iloc[index]["UserGroup"])
        landingpage_blank = pd.isna(df.iloc[index]["LandingURL"])
        redirect_type_blank = pd.isna(df.iloc[index]["RedirectionType"])
        print(domain_blank)
        
        if domain_blank:
            messages.append(f"Row {index+1}: ❌ Domain is blank.)")
        else:
            messages.append(f"Row {index+1}: ✅ Domain is OK")

        if usergroup_blank:
            messages.append(f"Row {index+1}: ❌ UserGroup is blank.)")
        else:
            messages.append(f"Row {index+1}: ✅ UserGroup is OK")
            
        if landingpage_blank:
            messages.append(f"Row {index+1}: ❌ landingpage is blank.)")
        else:
            messages.append(f"Row {index+1}: ✅ landingpage is OK")

        if redirect_type_blank:
            messages.append(f"Row {index+1}: ❌ Redirect Type is blank.")
        else:
            messages.append(f"Row {index+1}: ✅ Redirect Type is OK")
        
        print(messages)
        
open_and_show()