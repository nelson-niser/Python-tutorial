from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Prime Link Stock Management")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (screenWidth, screenHeight))


header = Label(root, text="PRIME LINK", anchor=CENTER, padx=10, pady=3,)


# img = ImageTk.PhotoImage(Image.open("img.jpg"))
# img_label = Label(image=img)



class iTile:
    def __init__(self, name, codeNum, quantity, price):
        self.name = name
        self.codeNum = codeNum
        self.quantity = quantity
        self.price = price

item_list = []
listbox = Listbox(root)

def add_item():
    add_dialog = Tk()
    add_dialog.title("Add Item")

    label_0 = Label(add_dialog, text="Name")
    item_name = Entry(add_dialog)
    item_name.insert(0, "Item Name")
    label_1 = Label(add_dialog, text="Code No")
    item_codeNum = Entry(add_dialog)
    item_codeNum.insert(0, "000")
    label_2 = Label(add_dialog, text="Quantity")
    item_quantity = Entry(add_dialog)
    item_quantity.insert(0, "1")
    label_3 = Label(add_dialog, text="Price")
    item_price = Entry(add_dialog)
    item_price.insert(0, "0")
    
    add_button = Button(add_dialog, text="Confirm", padx=22, command = lambda: save_item(add_dialog, item_name, item_codeNum, item_quantity, item_price))

    label_0.grid(row=0, column=0)
    item_name.grid(row=0, column=1)
    label_1.grid(row=1, column=0)
    item_codeNum.grid(row=1, column=1)
    label_2.grid(row=2, column=0)
    item_quantity.grid(row=2, column=1)
    label_3.grid(row=3, column=0)
    item_price.grid(row=3, column=1)
    add_button.grid(row=4, column=1)

    add_dialog.mainloop()
    
def save_item(add_dialog, item_name, item_codeNum, item_quantity, item_price):
    name = str(item_name.get())
    codeNum = str(item_codeNum.get())
    quantity = str(item_quantity.get())
    price = str(item_price.get())
    iTile_0 = iTile(name, codeNum, quantity, price)
    item_list.append(iTile_0)
    listbox.insert(END, name)
    add_dialog.destroy()

Add = Button(root, text="Add item", padx=22, command = add_item)
# Need def modification for del to delete from item_list
Del = Button(root, text="Delete", padx=30, command =lambda listbox=listbox: listbox.delete(ANCHOR))

##################################################
var0 = StringVar()
var0 = "NOT SELECTED"
item_description_name = Label(text = var0)

var1 = StringVar()
var1 = "NOT SELECTED"
item_description_codeNum = Label(text = var1)

var2 = StringVar()
var2 = "NOT SELECTED"
item_description_quantity = Label(text = var2)

var3 = StringVar()
var3 = "NOT SELECTED"
item_description_price = Label(text = var3)
#################################################

def print_selection():
    value = listbox.get(ACTIVE)
    for elems in item_list:
        if value == elems.name:
            item_description_name.config(text = elems.name)
            item_description_codeNum.config(text = elems.codeNum)
            item_description_quantity.config(text = elems.quantity)
            item_description_price.config(text = elems.price)

        else:
            pass
    



select_button = Button(root, text="Select", padx=30, command = print_selection)


item_description_0 = Label(text = "Name: ", anchor=E, borderwidth=4)
item_description_1 = Label(text = "Code No: ", anchor=E, borderwidth=4)
item_description_2 = Label(text = "Quantity: ", anchor=E, borderwidth=4)
item_description_3 = Label(text = "Price: ", anchor=E, borderwidth=4)

header.grid(row=0, column=0, columnspan=2)

Add.grid(row=1, column=0)
Del.grid(row=2, column=0)

listbox.grid(row=1, column=1, rowspan=9998)

item_description_0.grid(row=1, column=3)
item_description_name.grid(row=1, column=4)
item_description_codeNum.grid(row=2, column=4)
item_description_quantity.grid(row=3, column=4)
item_description_price.grid(row=4, column=4)
item_description_1.grid(row=2, column=3)
item_description_2.grid(row=3, column=3)
item_description_3.grid(row=4, column=3)
select_button.grid(row=5, column=4)



root.mainloop()