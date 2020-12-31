from tkinter import *
from tkinter import messagebox

from db import Database

db=Database('database.db')
# db.insert("4GB DDR4 Ram", "RAM", "simlim", "160")

#Functions
def populate():
    summary.delete(0,END)
    for row in db.fetch():
        summary.insert(END,row)

def add_item():
    if product.get() =='' or product_type.get()=='' or Retailer.get()=='' or price.get()=='':
        messagebox.showerror("Error","Please fill in all fields!")
        return
    db.insert(product.get(),product_type.get(),Retailer.get(),price.get())
    summary.delete(0, END)
    summary.insert(END,(product.get(),product_type.get(),Retailer.get(),price.get()))
    clear_text()
    populate()

def clear_item():
    # print('Clear')
    clear_text()

def update_item():
    db.update(selected_item[0],product.get(),product_type.get(),Retailer.get(),price.get())
    populate()
    # print('Update')


def select_item(event):
    try:
        global selected_item
        index = summary.curselection()[0]
        selected_item=summary.get(index)
        # print(selected_item)

        #display the data when selected
        product_entry.delete(0,END)
        product_entry.insert(END,selected_item[1])
        product_type_entry.delete(0,END)
        product_type_entry.insert(END,selected_item[2])
        Retailer_entry.delete(0,END)
        Retailer_entry.insert(END,selected_item[3])
        price_entry.delete(0,END)
        price_entry.insert(END,selected_item[4])
    except IndexError:
        pass




def remove_item():
    # print('Remove')
    db.remove(selected_item[0])
    populate()
    clear_text()


def clear_text():
    #clear text fields once deleted
    product_entry.delete(0, END)
    product_type_entry.delete(0, END)
    Retailer_entry.delete(0, END)
    price_entry.delete(0, END)


#Initialise tkinter app
app = Tk()

#Application properties
app.title('Purchase Planner')
app.geometry('650x400')

#Widgets

#1. Product widget
product = StringVar()
product_label = Label(app,text='Product Name',font=('bold',12),pady=20,padx=20)
product_label.grid(column=0,row=0,sticky=W)
product_entry = Entry(app,textvariable=product)
product_entry.grid(column=1,row=0)

#2. Product type
product_type = StringVar()
product_type_label = Label(app,text='Product Type',font=('bold',12),padx=10)
product_type_label.grid(column=2,row=0,sticky=W)
product_type_entry = Entry(app,textvariable=product_type)
product_type_entry.grid(column=3,row=0)

#3. Retailer widget
Retailer = StringVar()
Retailer_label = Label(app,text='Retailer Name',font=('bold',12),padx=20)
Retailer_label.grid(column=0,row=1,sticky=W)
Retailer_entry = Entry(app,textvariable=Retailer)
Retailer_entry.grid(column=1,row=1)

#4. Price widget
price = StringVar()
price_label = Label(app,text='Price ',font=('bold',12),padx=10)
price_label.grid(column=2,row=1,sticky=W)
price_entry = Entry(app,textvariable=price)
price_entry.grid(column=3,row=1)


#5. Summary widget 
#This will display the list of all the data we have saved so far
summary=Listbox(app,height=8,width=50)
summary.grid(row=3,column=0,rowspan=6,columnspan=3,pady=20,padx=20)

#Bind select
summary.bind('<<ListboxSelect>>', select_item)
#6.Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,column=3)

#7. Link scrollbar to summary 
summary.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=summary.yview)

#8. Buttons
add_button = Button(app,text='Add product',width=12,command=add_item)
add_button.grid(row=2,column=0,pady=20)

remove_button = Button(app,text='Remove product',width=12,command=remove_item)
remove_button.grid(row=2,column=1)

update_button = Button(app,text='Update product',width=12,command=update_item)
update_button.grid(row=2,column=2)

clear_button = Button(app,text='Clear product',width=12,command=clear_item)
clear_button.grid(row=2,column=3)


#Populate data
populate()
#Event loop
app.mainloop()