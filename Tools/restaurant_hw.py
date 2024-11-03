import tkinter as tk

window = tk.Tk()
window.title("Restaurant Order UI")
window.geometry("800x550")
window.configure(bg="#25CED1")

email_label = tk.Label(window, text="Email Address:", font=("Helvetica", 20), fg="black", bg="#FF8A5B")
email_label.pack(pady=10)
email_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
email_entry.pack(pady=5)

password_label = tk.Label(window, text="Password:", font=("Helvetica", 20), fg="black", bg="#FF8A5B")
password_label.pack(pady=10)
password_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
password_entry.pack(pady=5)

food_label = tk.Label(window, text="What food would you like: (e.g., Chicken Sandwich, B.L.T, etc.)", font=("Helvetica", 20), fg="black", bg="#FF8A5B")
food_label.pack(pady=10)
food_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
food_entry.pack(pady=5)

beverage_label = tk.Label(window, text="What beverage would you like: (e.g., Cola, Fanta, etc.)", font=("Helvetica", 20), fg="black", bg="#FF8A5B")
beverage_label.pack(pady=10)
beverage_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
beverage_entry.pack(pady=5)

dessert_label = tk.Label(window, text="What dessert would you like: (e.g., Ice Cream, Chocolate Cake, etc.)", font=("Helvetica", 20), fg="black", bg="#FF8A5B")
dessert_label.pack(pady=10)
dessert_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
dessert_entry.pack(pady=5)

submit_button = tk.Button(window, text="Submit Order", font=("Helvetica", 20))
submit_button.pack(pady=30)

window.mainloop()