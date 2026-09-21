from tkinter import *

root = Tk()

#tytuł
root.title("Book scrapper")
#jak duże okno
root.geometry("350x200")

#menu
#menu = Menu(root)
#item = Menu(menu)
#item.add_command(label='new')
#menu.add_cascade(label='file', menu=item)
#root.config(menu=menu)



#entry label 
#txt = Entry(root, width=10)
#txt.grid(column=3, row=0)

#label
lbl = Label(root, text="Do you want to get info about book prices?")
lbl.grid(column=0,row=0)

#when button clicked
def clicked():
    lbl.configure(text="Fetching data now")
#    res = f"you wrote {txt.get()}"
#    lbl.configure(text=res)

def clicked2():
    lbl.configure(text="Goodbye")

#button
btn1 = Button(root, text="Yes", fg="blue", command=clicked)
btn1.grid(column=0, row=3)

btn2 = Button(root, text="No", fg="red", command=clicked2)
btn2.grid(column=1, row=3)

#execute
root.mainloop()

