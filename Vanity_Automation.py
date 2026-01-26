from tkinter import Tk, Label, Button, filedialog,Frame, Scrollbar, Text
import pandas as pd
import webbrowser
from PIL import Image, ImageTk

def create_scrollable_text(parent, width=240, height=15):
    frame = Frame(parent)
    frame.grid(sticky="w")

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text = Text(
        frame,
        width=width,
        height=height,
        yscrollcommand=scrollbar.set,
        wrap="none",
        font=("Consolas", 10)
    )
    text.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=text.yview)

    return frame, text

def open_and_show():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.config(state="disabled")
    proceed_button.grid_remove()
    
    df = pd.read_excel(file_path)

    input_text.config(state="normal")
    input_text.delete("1.0", "end")

    header = " | ".join(df.columns)
    input_text.insert("end", header + "\n")
    input_text.insert("end", "-" * len(header) + "\n")

    total_rows = len(df)
    missing_found = False

    for index, row in df.iterrows():

        domain_blank = pd.isna(row["Domain"]) or str(row["Domain"]).strip() == ""
        usergroup_blank = pd.isna(row["UserGroup"]) or str(row["UserGroup"]).strip() == ""
        landingpage_blank = pd.isna(row["LandingUrl"]) or str(row["LandingUrl"]).strip() == ""
        redirect_type_blank = pd.isna(row["RedirectionType"])

        row_text = " | ".join(
            "" if pd.isna(val) else str(val)
            for val in row.values
        ) + "\n"

        if domain_blank or usergroup_blank or landingpage_blank or redirect_type_blank:
            input_text.insert("end", row_text, "blank_row")
            missing_found = True
        else:
            input_text.insert("end", row_text, "normal_row")

    if missing_found:
        status_label.config(
            text=f"Status: Data loaded successfully with {total_rows} rows. "
                 f"Rows highlighted in red if any data is missing."
        )
        validate_button.grid_remove()
    else:
        status_label.config(
            text=f"Status: Data loaded successfully with {total_rows} rows. "
                 f"No missing data found. Kindly proceed to validate."
        )

    input_text.config(state="disabled")    

def validate_data():
    global df
    if df is None:
        status_label.config(
            text="Status: Please upload a file before validating."
        )
        return    
    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    proceed_button.grid_remove()

    file_path1 = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    ref_df = pd.read_excel(file_path1)

    domain_list = ref_df["Domain"].astype(str).str.strip().str.lower().values
    usergroup_list = ref_df["UserGroup"].astype(str).str.strip().str.lower().values

    Error_found = False
    all_messages = []

    for index, row in df.iterrows():
        domain = str(row["Domain"]).strip().lower()
        usergroup = str(row["UserGroup"]).strip().lower()
        redirect_type = int(row["RedirectionType"])

        all_messages.append(f"Row {index+1}:")

        if domain in domain_list:
            Error_found = True
            all_messages.append(f"❌ Domain exists ({domain})")
        else:
            all_messages.append("✅ Domain OK")

        if usergroup in usergroup_list:
            Error_found = True
            all_messages.append(f"❌ UserGroup exists ({usergroup})")
        else:
            all_messages.append("✅ UserGroup OK")

        if redirect_type == 301:
            all_messages.append("✅ Redirect Type OK (301)")
        else:
            Error_found = True
            all_messages.append(f"❌ Redirect Type invalid ({redirect_type})")

        all_messages.append("-" * 100)

    result_text.delete("1.0", "end")
    result_text.insert("end", "\n".join(all_messages))
    result_text.config(state="disabled")

    if Error_found:
        status_label.config(
            text="Status: Validation completed with errors. Click on Quit to exit and fix the issues."
        )
        proceed_button.grid_remove()
    else:
        status_label.config(
            text="Status: Validation successful. All rows good. Click on Proceed button to continue to Link Studio."
        )
        proceed_button.grid()

    
def proceed_action():
    status_label.config(text="Status: Proceeding with the next steps...")
    webbrowser.open("https://linkstudio.dell.com/home")

def clear_screen():
    global df
    df = None

    input_text.config(state="normal")
    input_text.delete("1.0", "end")
    input_text.config(state="disabled")

    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.config(state="disabled")

    status_label.config(text="Status: Screen cleared. Please upload a new file.")

    proceed_button.grid_remove()

root = Tk()
root.title("Vanity Automation.py")
root.state('zoomed')
# root.overrideredirect(True)

header_frame = Frame(root, bg="#e0e0e0", height=100)
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
header_frame.grid_propagate(False)

logo_img = Image.open("logo.png")
logo_img = logo_img.resize((81,81))
logo = ImageTk.PhotoImage(logo_img)

logo_label = Label(header_frame, image=logo, bg="#93b8ba")
logo_label.image = logo
logo_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")

header_title = Label(header_frame,text="Vanity Validation & Update Tool",font=("Arial", 18, "bold"),bg="#e0e0e0")
header_frame.grid_columnconfigure(0, weight=0)
header_frame.grid_columnconfigure(1, weight=1)
# header_title.grid(row=0, column=1, sticky="w", padx=10)
header_title.place(relx=0.5, rely=0.5,anchor="center")

main_frame = Frame(root)
main_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

open_button = Button(main_frame, text="Open File", command=open_and_show, width=15,bg="white",fg="black")
open_button.grid(row=1, column=0, padx=15, pady=10, sticky="w")

input_frame, input_text = create_scrollable_text(main_frame, height=12)
input_text.tag_configure("blank_row", foreground="red")
input_text.tag_configure("normal_row", foreground="black")
input_frame.grid(row=2, column=0, padx=15, pady=10, sticky="w")

validate_button = Button(main_frame, text="Validate Data", command=validate_data, width=15,bg="skyblue",fg="black")
validate_button.grid(row=5, column=0, padx=15, pady=10, sticky="w")

result_frame, result_text = create_scrollable_text(main_frame, height=18)
result_frame.grid(row=6, column=0, padx=15, pady=10, sticky="w")

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

clear_button = Button(main_frame,text="Clear Screen",command=clear_screen,width=15,bg="orange",fg="black")
clear_button.grid(row=3, column=0, padx=15, pady=10, sticky="w")

footer_frame = Frame(root, bg="#e0e0e0", height=80)
footer_frame.grid(row=2, column=0, columnspan=3, sticky="ew")
footer_frame.grid_propagate(False)
footer_label = Label(footer_frame,text="© 2026 Internal Vanity Updation Tool | Designed by Karuna Sagar| Built by Shiv Ravinder",bg="#e0e0e0",font=("Arial", 9))
footer_label.place(relx=0.5, rely=0.5, anchor="center")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)

# simpledialog.askstring("Input", "Enter your name:")

root.mainloop()
