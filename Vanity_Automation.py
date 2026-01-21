from tkinter import Tk, Label, Button, filedialog
import pandas as pd
import webbrowser
from tkinter import Frame
from PIL import Image, ImageTk

def open_and_show():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    df = pd.read_excel(file_path)
    result_label.config(text=df.to_string(index=False, justify="right"))
    status_label.config(text=f"Status: File loaded successfully ({len(df)} rows)")

def validate_data():
    file_path1 = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    ref_df = pd.read_excel(file_path1)
    domain_list = ref_df["Domain"].astype(str).str.strip().str.lower()
    usergroup_list = ref_df["UserGroup"].astype(str).str.strip().str.lower()
    Error_found = False

    for index,row in df.iterrows():
        domain = str(row["Domain"]).strip().lower()
        usergroup = str(row["UserGroup"]).strip().lower()
        redirect_type = int(row["RedirectionType"])
        messages = []
        
        if domain in domain_list.values:
            Error_found = True
            messages.append(f"Row {index+1}: ❌ Domain exists ({domain})")
        else:
            messages.append(f"Row {index+1}: ✅ Domain OK")

        if usergroup in usergroup_list.values:
            Error_found = True
            messages.append(f"Row {index+1}: ❌ UserGroup exists ({usergroup})")
        else:
            messages.append(f"Row {index+1}: ✅ UserGroup OK")

        if redirect_type == 301:
            messages.append(f"Row {index+1}: ✅ Redirect Type OK (301)")
        else:
            Error_found = True
            messages.append(f"Row {index+1}: ❌ Redirect Type invalid ({redirect_type})")

        messages.append("-" * 40)

    result_label1.config(text="\n".join(messages))

    if Error_found:
        status_label.config(text="Status: Validation completed with errors.")
        proceed_button.grid_remove()
    else:
        status_label.config(text="Status: Validation successful. All rows good.")
        proceed_button.grid()
    
def proceed_action():
    status_label.config(text="Status: Proceeding with the next steps...")
    webbrowser.open("https://www.dell.com")

root = Tk()
root.title("Vanity Automation.py")
root.state('zoomed')
root.overrideredirect(True)

header_frame = Frame(root, bg="#f5f5f5", height=80)
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
header_frame.grid_propagate(False)

logo_img = Image.open("logo.png")
logo_img = logo_img.resize((60, 60))
logo = ImageTk.PhotoImage(logo_img)

logo_label = Label(header_frame, image=logo, bg="#f5f5f5")
logo_label.image = logo
logo_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")

header_title = Label(header_frame,text="Vanity Validation Tool",font=("Arial", 18, "bold"),bg="#f5f5f5")
header_frame.grid_columnconfigure(0, weight=0)
header_frame.grid_columnconfigure(1, weight=1)
# header_title.grid(row=0, column=1, sticky="w", padx=10)
header_title.place(relx=0.5, rely=0.5,anchor="center")

main_frame = Frame(root)
main_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

open_button = Button(main_frame, text="Open File", command=open_and_show, width=15,bg="white",fg="black")
open_button.grid(row=1, column=0, padx=15, pady=10, sticky="w")

result_label = Label(main_frame, text="", justify="left", anchor="nw", font=("Consolas", 10))
result_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")

validate_button = Button(main_frame, text="Validate Data", command=validate_data, width=15,bg="skyblue",fg="black")
validate_button.grid(row=5, column=0, padx=15, pady=10, sticky="w")

result_label1 = Label(main_frame, text="", justify="left", anchor="nw", font=("Consolas", 10))
result_label1.grid(row=6, column=0, padx=15, pady=10, sticky="w")

# result_label2 = Label(main_frame, text="", justify="left", anchor="nw", font=("Consolas", 10))
# result_label2.grid(row=7, column=0, padx=15, pady=10, sticky="w")

# result_label3 = Label(main_frame, text="", justify="left", anchor="nw", font=("Consolas", 10))
# result_label3.grid(row=8, column=0, padx=15, pady=10, sticky="w")

proceed_button = Button(main_frame, text="Proceed", command=proceed_action, width=15,bg="green",fg="white")
proceed_button.grid(row=9, column=0, padx=15, pady=10, sticky="w")
proceed_button.grid_remove() 

status_label = Label(main_frame, text="Status: Ready")
status_label.grid(row=10, column=0, padx=15, pady=10, sticky="w")

quit_button = Button(main_frame, text="Quit", command=root.quit, width=15,bg="red",fg="white")
quit_button.grid(row=11, column=0, padx=15, pady=10, sticky="w")

footer_frame = Frame(root, bg="#e0e0e0", height=80)
footer_frame.grid(row=2, column=0, columnspan=3, sticky="ew")
footer_frame.grid_propagate(False)
footer_label = Label(footer_frame,text="© 2026 Internal QA Tool | All Rights Reserved",bg="#e0e0e0",font=("Arial", 9))
footer_label.place(relx=0.5, rely=0.5, anchor="center")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)

# simpledialog.askstring("Input", "Enter your name:")

root.mainloop()
