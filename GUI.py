import tkinter as tk
from Classes.owanova import Anova

entries = []
lsd = 0
f_ratio = 0
f_table = 0
liste = list()
def calc():
    entryChecker = []
    try:
        if isinstance(float(entryAlpha.get()),float):
            print("alpha passed")
            for i in range(len(entries)):
                if not isinstance(eval("[" + entries[i].get()+ "]"),list) or entries[i].get() == "":
                    print("error")
                else:
                    print("success for number " + str(i))
                    entryChecker.append(entries[i].get())
            if len(entryChecker) == len(entries):
                entryParser = []
                for i in range(len(entries)):
                    listEntry = entries[i].get().split(",")
                    entryParser.append(listEntry)
                anova1 = Anova(0.05,entryParser)
                lsd,f_ratio,f_table, liste = anova1.anova()
                return lsd,f_ratio,f_table, liste

    except Exception as e:
        print(str(e) + "lol")

def create_entry():
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)


root = tk.Tk()
root.title("Statistical Data Analysis")
root.geometry("1000x700")

frame = tk.Frame(root)
frame.pack()

label1 = tk.Label(frame, text="First inputs fields are for number sequences. Make sure the numbers are separated by commas. The last field is for your alpha value, which must be of type float.")
label1.pack()




for i in range(3):
    create_entry()
    
entryAlpha = tk.Entry(root)
entryAlpha.pack()

button = tk. Button(frame, text="Run",command=calc)
button.pack()
label2 = tk.Label(frame,text=f_ratio)
label2.pack()

root.mainloop()