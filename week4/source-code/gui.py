import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("Gui")

name_label = tk.Label(window, text = "Enter your name: ")
age_label = tk.Label(window, text = "Enter your age: ")

name_entry = tk.Entry(window)
age_entry = tk.Entry(window)

submit_button = tk.Button(window, text = "Submit")

name_label.pack()
age_label.pack()
name_entry.pack()
age_entry.pack()
submit_button.pack()

window.mainloop()