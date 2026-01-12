
def validate_data():
    global df
    validate_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv")])
    df_validate = pd.read_excel(validate_path)
    if df["Domain", "UserGroup"] in df_validate["Domain", "UserGroup"]:
        status_label.config(text="Status: No matching data found, Data is good to use")
    else:
        status_label.config(text="Status: Errors found in data, please check" + matches.to_string(index=False))
    
validate_data()