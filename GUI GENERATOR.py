from tkinter import *
from tkinter import ttk

root = Tk()
root.title("GUI Generator")
root.geometry("600x600")
root.configure(bg="#98EECC")

class elementbtn:
    def __init__(self):
        print("btn")
    def c(self):
        messagebox.showinfo("Message!", "This was created using the Classes/Objects concept.")
    def Creator(self):
        if combo.get() == "label":
            lbl=Label(root, text="Label", bg="#98EECC", fg="black")
            lbl.pack(padx=10, pady=10)
        if combo.get() == "button":
            btn=Button(root, text="Button", bg="#98EECC", fg="black", command=self.c)
            btn.pack(padx=10, pady=10)
        if combo.get() == "dropdown":
            e2 = ["hello", "cool", "happycoding"]
            combo2 = ttk.Combobox(root, state="r", values=e2)
            style = ttk.Style()
            style.map('TCombobox', fieldbackground=[('readonly','#98EECC')])
            style.map('TCombobox', selectbackground=[('readonly', 'black')])
            style.map('TCombobox', selectforeground=[('readonly', '#98EECC')])
            combo2.pack(padx=10, pady=10)

button = elementbtn()

e = ["label", "button", "dropdown"]
combo = ttk.Combobox(root, state="r", values=e)
style = ttk.Style()

style.map('TCombobox', fieldbackground=[('readonly','#98EECC')])
style.map('TCombobox', selectbackground=[('readonly', 'black')])
style.map('TCombobox', selectforeground=[('readonly', '#98EECC')])

combo.pack(padx=10, pady=10)

cbtn = Button(root, text="Create Element", bg="black", fg="#98EECC", command=button.Creator)
cbtn.pack(padx=10, pady=10)

root.mainloop()