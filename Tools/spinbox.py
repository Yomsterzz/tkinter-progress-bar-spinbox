import tkinter as tk

def get_data():
    print(spin.get(), ". Recieved from spinbox 1")
    print(spin2.get(), ". Recieved from spinbox 2")
    print(spin3.get(), ". Recieved from spinbox 3")


window = tk.Tk()
window.title("Spinbox")
window.geometry("800x600")

spin = tk.Spinbox(window, values=("apple", "banana", "cherry", "orange"), command=get_data)
spin2 = tk.Spinbox(window, from_=1, to=10, increment=0.1, format='%04.1f', command=get_data)
spin3 = tk.Spinbox(window, from_=23, to=45, state="readonly", command=get_data)

spin.pack(padx=20, pady=20)
spin2.pack(padx=20, pady=20)
spin3.pack(padx=20, pady=20)

window.mainloop()