import pandas as pd

def validate_data():
    df = pd.read_excel(r"C:\Users\Ravin\OneDrive\Desktop\vanity.xlsx")
    df1 = pd.read_excel(r"C:\Users\Ravin\OneDrive\Desktop\validatedata.xlsx")

    search_domain = str(df.iloc[0]["Domain"]).strip().lower()

    domain_list = df1["Domain"].astype(str).str.strip().str.lower()

    if search_domain in domain_list.values:
        print(f"✅ Match found: {search_domain}")
    else:
        print(f"❌ No match found: {search_domain}")

validate_data()
