from tkinter import Tk, Label, Button
from filehandling import fileopen

def open_and_show():
    df = fileopen()
    result_label.config(text=str(df.head()))
    status_label.config(text="Status: File opened successfully and validated")

root = Tk()
root.title("Testing window for project1.py")
root.geometry("1000x1000")

label = Label(root, text="Project testing window!")
label.pack(pady=100)

button = Button(root, text="Open file", command=open_and_show)
button.pack()

result_label = Label(root, text="")
result_label.pack(pady=20)

status_label = Label(root, text="Status: Ready")
status_label.pack(side="bottom", pady=10)

button_quit = Button(root, text="Quit", command=root.quit)
button_quit.pack(side="bottom", pady=10)

root.mainloop()