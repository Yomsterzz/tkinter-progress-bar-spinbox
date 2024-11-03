import tkinter as tk

def update_data():
    data = entry1.get()
    label1.config(text=data)
    entry1.delete(0,tk.END)
    
window = tk.Tk()
window.title("First Project!")
window.geometry("800x600")
window.configure(bg=("blue"))

# first widget: text (label)
label1 = tk.Label(window, text="Look at me! I'm a label!", font=("Helvetica", 38), fg="red", bg="green", width=20, height=2, justify=tk.LEFT)
label2 = tk.Label(window, text="Look at me! I'm a label!", font=("Helvetica", 38), fg="red", bg="green", width=20, height=2, justify=tk.LEFT)
# 3 ways to position widgets: pack, grid and place
# pack: 
label1.pack(pady=30)
label2.pack()

# side property lets you choose which side the widget will align to. there are 4 sides.

# second widget: button
button1 = tk.Button(window, text="Click ME!", font=("Helvetica", 38), command=window.destroy)
button1.pack(pady=30)

button2 = tk.Button(window, text="Click ME!", font=("Helvetica", 38), command=update_data)
button2.pack(pady=30)

# last widget: input (entry)
entry1 = tk.Entry(window, fg="green", bg="red", justify=tk.CENTER)
entry1.pack()


window.mainloop()