"""
To build an database application for desktop
that can all user to:

box: Author ,year,ISBN,book,Text box
Scroll bar
buttons:view all
        Search entry
        Add entry
        update
        delete
        close
"""
from tkinter import *
import backend

def view_command():
    list.delete(0,END)
    for rows in backend.view():
        list.insert(END,rows)

def search_command():
    list.delete(0,END)
    for rows in backend.search(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()):
        list.insert(END,rows)

def add_command():
    if len(title_txt.get()+author_txt.get()+year_txt.get()+isbn_txt.get())!=0:
        backend.insert(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())
        list.delete(0,END)
        list.insert(END,(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()))

def update_command():
    backend.update(selected_row[0],title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())
    view_command()

def delete():
    backend.delete(selected_row[0])
    list.delete(0,END)
    view_command()

def select(event):
    try:
        global selected_row
        index=list.curselection()
        selected_row=list.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
    except:
        pass


window=Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Year")
l2.grid(row=1,column=0)

l3=Label(window,text="Author")
l3.grid(row=0,column=2)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_txt=StringVar()
e1=Entry(window,textvariable=title_txt)
e1.grid(row=0,column=1)

year_txt=StringVar()
e2=Entry(window,textvariable=year_txt)
e2.grid(row=1,column=1)

author_txt=StringVar()
e3=Entry(window,textvariable=author_txt)
e3.grid(row=0,column=3)

isbn_txt=StringVar()
e4=Entry(window,textvariable=isbn_txt)
e4.grid(row=1,column=3)

list=Listbox(window,height=6,width=35)
list.grid(row=2,column=0,rowspan=6,columnspan=2)

scrollbar=Scrollbar(window)
scrollbar.grid(row=2,column=2,rowspan=6)


list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list.yview)

list.bind('<<ListboxSelect>>',select)


b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
