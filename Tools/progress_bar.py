import tkinter as tk
from tkinter import ttk

def add_progress():
    progress2.start()


window = tk.Tk()
window.title("Progress Bar")
window.geometry("800x600")
window.configure(bg="blue")

progressvalue = 20

progress1 = ttk.Progressbar(window, length=300, mode="determinate", orient="vertical")
progress2 = ttk.Progressbar(window, length=300, mode="indeterminate", orient="horizontal")
button1 = tk.Button(window, text="Click ME!", font=("Helvetica", 38), command=add_progress)

progress1["value"] = 50
progress1.pack()


progress2.pack()

button1.pack(pady=30)

window.mainloop()