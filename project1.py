from tkinter import Tk, Label, Button, filedialog,simpledialog
from filehandling import fileopen
import pandas as pd

def open_and_show():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv")])
    df = pd.read_excel(file_path).head(1)
    result_label.config(text=df.to_string(index=False))
    status_label.config(text="Status: File opened successfully and data loaded")

def validate_data():
    validate_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv")])
    df_validate = pd.read_excel(validate_path)
    matches = df_validate.merge(df, how='inner', on=['Domain','Region'])
    if matches.empty:
        status_label.config(text="Status: No matching data found, Date is good to use")
    else:
        status_label.config(text="Status: Errors found in data, please check" + matches.to_string(index=False))

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
validate_button.grid(row=1, column=1, padx=15, pady=10, sticky="w")

status_label = Label(root, text="Status: Ready")
status_label.grid(row=3, column=0, padx=15, pady=10, sticky="w")

quit_button = Button(root, text="Quit", command=root.quit, width=15)
quit_button.grid(row=4, column=0, padx=15, pady=10, sticky="w")

root.grid_columnconfigure(0, weight=1)

# simpledialog.askstring("Input", "Enter your name:")

root.mainloop()