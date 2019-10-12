from tkinter import *

root = Tk()
rootTitle = "Body Mass Index"
root.resizable(0, 0)
root.configure(background="#3f51b5")

def cal():
    height = float(inputH.get())
    weight = float(inputW.get())
    result = weight / ((height / 100) ** 2)
    outputBmi["text"] = "%.2f" % result
    if result > 18.5:
        if result > 24.9:
            if result > 25:
                if result > 30:
                    outputCate["text"] = "Obese"
            else:
                outputCate["text"] = "Overweight"
        else:
            outputCate["text"] = "Normal"
    else:
        outputCate["text"] = "Underweight"


head = Label(root, text="Body Mass Index", font=("Verdana", 20, "bold"), bg="#3f51b5", fg="white")
head.grid(row=0, columnspan=2, pady=15)

h = Label(root, text="Height: (Cm.)", font=("Verdana", 15), bg="#3f51b5", fg="white")
h.grid(row=1, column=0, pady=5)
w = Label(root, text="Weight: (Kg.)", font=("Verdana", 15), bg="#3f51b5", fg="white")
w.grid(row=2, column=0, padx=5)

inputH = Entry(root, font=("Verdana", 15), justify="center", bg="#757de8", fg="black")
inputH.grid(row=1, column=1, pady=5)
inputW = Entry(root, font=("Verdana", 15), justify="center", bg="#757de8", fg="black")
inputW.grid(row=2, column=1, pady=5)

button = Button(root, text="Calculate", command=cal, font=("Verdana", 15), bg="#002984", fg="white")
button.grid(row=3, columnspan=2, pady=5)

bmi = Label(root, text="BMI: ", font=("Verdana", 15), bg="#3f51b5", fg="white")
bmi.grid(row=4, column=0, pady=5)
cate = Label(root, text="Category: ", font=("Verdana", 15), bg="#3f51b5", fg="white")
cate.grid(row=5, column=0, pady=5)

outputBmi = Label(root, relief="groove", font=("Verdana", 15), bg="#757de8", fg="black")
outputBmi.grid(row=4, column=1, pady=5)
outputCate = Label(root, relief="groove", font=("Verdana", 15), bg="#757de8", fg="black")
outputCate.grid(row=5, column=1, pady=5)

root.mainloop()
