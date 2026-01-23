import pandas as pd

def open_and_show():
    global df
    df = pd.read_excel(r"C:\Users\Shiv_Ravinder_Singh\Downloads\intake_template_validated.xlsx")
    total_rows =  len(df["Domain"])
    print(total_rows)
    blank = pd.isna(df.iloc[0]["Domain"])
    print(blank)
    
    for index,row in df.iterrows():
        domain = str(row["Domain"]).strip().lower()
        usergroup = str(row["UserGroup"]).strip().lower()
        landingpage = str(row["LandingURL"]).strip().lower()
        redirect_type = int(row["RedirectionType"])
        messages = []
        domain_blank = pd.isna(domain)
        usergroup_blank = pd.isna(usergroup)
        landingpage_blank = pd.isna(landingpage)
        redirect_type_blank = pd.isna(redirect_type)
        
        if domain_blank:
            messages.append(f"Row {index+1}: ❌ Domain is blank.)")
        else:
            messages.append(f"Row {index+1}: ✅ Domain OK")

        if usergroup_blank:
            messages.append(f"Row {index+1}: ❌ UserGroup is blank.)")
        else:
            messages.append(f"Row {index+1}: ✅ UserGroup OK")
            
        if landingpage_blank:
            messages.append(f"Row {index+1}: ❌ landingpage is blank.)")
        else:
            messages.append(f"Row {index+1}: ✅ UserGroup OK")

        if redirect_type_blank:
            messages.append(f"Row {index+1}: ❌ Redirect Type is blank.")
        else:
            messages.append(f"Row {index+1}: ✅ Redirect Type is OK")
        
    print(messages)
        
open_and_show()