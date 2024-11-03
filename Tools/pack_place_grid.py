import tkinter as tk


window = tk.Tk()
window.title("First Project!")
window.geometry("800x600")
window.configure(bg=("blue"))

# first widget: text (label)
label1 = tk.Label(window, text="Look at me! I'm a label!", bd=10, relief="ridge")
label2 = tk.Label(window, text="Look at me! I'm a label!")
label3 = tk.Label(window, text="Look at me! I'm a label!")
# 3 ways to position widgets: pack, grid and place
# pack: 
"""
label1.pack(pady=30, fill=tk.Y, anchor="w")
label2.pack(expand=True)
label3.pack(anchor="sw")
"""

# grid:
"""
label1.grid(row=0, column=0, padx=5, pady=5, columnspan=2, rowspan=2)
label2.grid(row=0, column=2, sticky="ew", ipadx=30, ipady=30)
label3.grid(row=2, column=0)
"""

#place:
label1.place(relx=0.5, rely=0.2, anchor=tk.CENTER, width=200, height=100, bordermode=tk.OUTSIDE)



# side property lets you choose which side the widget will align to. there are 4 sides.

window.mainloop()