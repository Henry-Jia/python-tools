# Number System convertor.


from tkinter import *
from tkinter import messagebox

def giver(str,l):
    return int(str,l)


def inite():
    d = val1.get()
    p = str(el.get())
    try:
        if d=='Hexadecimal':
            res = int(p,16)
        if d=='Binary':
            res = int(p,2)
        if d=='Octal':
            res = int(p,8)
        if d=='Integer':
            res = "same value"
        res= str(res)
        no = "RESULT : INTEGER FORMAT  : "
        no += res
        no += " "*100
        lbl = Label(text=no, bg='pink', fg='blue', font=for_font).place(x=200, y=500)

    except:
        messagebox.showinfo("Error","Some Error occurred")


def bine():
    d = val1.get()
    p = str(el.get())
    try:
        if d == 'Hexadecimal':
            ip = giver(p,16)
            res = str(bin(ip))
        if d == 'Binary':
            res = "lo   same value"
        if d == 'Octal':
            ip = giver(p,8)
            res = str(bin(ip))
        if d == 'Integer':
            res = str(bin(int(p)))
        res = str(res[2:])
        no = "RESULT : BINARY FORMAT : "
        no += res
        no += " " * 50
        lbl = Label(text=no, bg='pink', fg='blue', font=for_font).place(x=200, y=500)

    except:
        messagebox.showinfo("Error", "Some Error occurred")



def octe():
    d = val1.get()
    p = str(el.get())
    try:
        if d == 'Hexadecimal':
            ip = giver(p, 16)
            res = str(oct(ip))
        if d == 'Binary':
            ip = giver(p,2)
            res = str(oct(ip))
        if d == 'Octal':
            res = "lo    same value"
        if d == 'Integer':
            res = str(oct(int(p)))
        res = str(res[2:])
        no = "RESULT : OCTAL FORMAT  : "
        no += res
        no += " " * 100
        lbl = Label(text=no, bg='pink', fg='blue',font=for_font).place(x=200, y=500)

    except:
        messagebox.showinfo("Error", "Some Error occurred")


def hexe():
    d = val1.get()
    p = str(el.get())
    try:
        if d == 'Hexadecimal':
            res = "lo   Same value"
        if d == 'Binary':
            ip = giver(p, 2)
            res = str(hex(ip))
        if d == 'Octal':
            ip = giver(p,8)
            res = str(hex(ip))
        if d == 'Integer':
            res = str(hex(int(p)))
        res = str(res[2:])
        no = "RESULT : HEXADECIMAL FORMAT  : "
        no += res
        no += " " * 100
        lbl = Label(text=no, bg='pink', fg='blue', font=for_font).place(x=200, y=500)

    except:
        messagebox.showinfo("Error", "Some Error occurred")

root = Tk()
root.title('Number system')
root.geometry('1360x768')

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(root, tearoff=0)
filemenu.add_command(label='New')
filemenu.add_command(label='Converter')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)

f = Frame(root, bg='pink', height=760, width=1360)
f.propagate(0)
f.pack()
for_font = ('Times', -40, 'bold')
el = Entry(f, width=30, bg='white', fg='blue', font=for_font)
el.place(x=500, y=50)
b1 = Button(f, text='Binary', font=for_font, bg='white', fg='blue', height=1, width=9, command=bine)
b1.place(x=100, y=200)
b2 = Button(f, text='Hexadecimal', font=for_font, bg='white', fg='blue', height=1, width=10, command=hexe)
b2.place(x=400, y=200)
b3 = Button(f, text='Octal', font=for_font, bg='white', fg='blue', height=1, width=9, command=octe)
b3.place(x=700, y=200)
b4 = Button(f, text='Integer', font=for_font, bg='white', fg='blue', height=1, width=9, command=inite)
b4.place(x=1000, y=200)
val1 = StringVar()
format = ('Hexadecimal', 'Binary', 'Octal', 'Integer')
s1 = Spinbox(f, textvariable=val1, values=format, font=for_font, width=15)
s1.place(x=100, y=50)
root.mainloop()
