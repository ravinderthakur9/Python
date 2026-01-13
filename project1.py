from tkinter import Tk, Label, Button, filedialog
import pandas as pd
import os

def open_and_show():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    df_transpose = pd.read_excel(file_path).head(1)
    df = df_transpose.transpose()
    df.columns = ["Values from intake sheet"]
    result_label.config(text=df.to_string(index=False,justify="right"))
    status_label.config(text="Status: File opened successfully and data loaded")

def validate_data():
    file_path1 = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    df1 = pd.read_excel(file_path1)
    search_domain = str(df.iloc[0]["Domain"]).strip().lower()
    domain_list = df1["Domain"].astype(str).str.strip().str.lower()
    search_usergroup = str(df.iloc[0]["UserGroup"]).strip().lower()
    usergroup_list = df1["UserGroup"].astype(str).str.strip().str.lower()
    redirect_type = int(df["RedirectionType"][0])

    Error_found = False
    
    if search_domain in domain_list.values:
        result_label1.config(text=f"Match found: Domain {search_domain}")
        Error_found = True
    else:
        result_label1.config(text=f"No match found: Domain {search_domain}")
    
    if search_usergroup in usergroup_list.values:
        result_label2.config(text=f"Match found: UserGroup {search_usergroup}")
        Error_found = True
    else:
        result_label2.config(text=f"No match found: UserGroup {search_usergroup}")

    if redirect_type == 301:
        result_label3.config(text=f"Redirection Type is good {redirect_type}")
    else:
        result_label3.config(text=f"Redirection Type is wrong as it is {redirect_type}")
        Error_found = True   

    if Error_found:
        status_label.config(text="Status: Data validated successfully and need to looked into as errors found.")
    else:
        status_label.config(text="Status: Data validated successfully and good to proceed.")

root = Tk()
root.title("Testing window for project1.py")
root.state('zoomed')
# filedialog.askopenfilename()

title = Label(root, text="Project testing window!", font=("Arial", 16))
title.grid(row=0, column=0, columnspan=2, pady=15,sticky="n")

open_button = Button(root, text="Open File", command=open_and_show, width=15)
open_button.grid(row=1, column=0, padx=15, pady=10, sticky="w")

result_label = Label(root, text="", justify="left", anchor="nw", font=("Consolas", 10))
result_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")

validate_button = Button(root, text="Validate Data", command=validate_data, width=15)
validate_button.grid(row=5, column=0, padx=15, pady=10, sticky="w")

result_label1 = Label(root, text="", justify="left", anchor="nw", font=("Consolas", 10))
result_label1.grid(row=6, column=0, padx=15, pady=10, sticky="w")

result_label2 = Label(root, text="", justify="left", anchor="nw", font=("Consolas", 10))
result_label2.grid(row=7, column=0, padx=15, pady=10, sticky="w")

result_label3 = Label(root, text="", justify="left", anchor="nw", font=("Consolas", 10))
result_label3.grid(row=8, column=0, padx=15, pady=10, sticky="w")

status_label = Label(root, text="Status: Ready")
status_label.grid(row=9, column=0, padx=15, pady=10, sticky="w")

quit_button = Button(root, text="Quit", command=root.quit, width=15)
quit_button.grid(row=10, column=0, padx=15, pady=10, sticky="w")

root.grid_columnconfigure(0, weight=1)

# simpledialog.askstring("Input", "Enter your name:")

root.mainloop()