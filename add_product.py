#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 22, 2021 01:07:35 AM PKT  platform: Windows NT

import platform
import sys
import sqlite3
import tkinter.messagebox as messagebox


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import add_product_support

a_checkPoint = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''

    global a_checkPoint

    a_checkPoint = False

    global val, w, root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', destroy_Toplevel1)
    add_product_support.set_Tk_var()
    top = Toplevel1(root)
    add_product_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    add_product_support.set_Tk_var()
    top = Toplevel1(w)
    add_product_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w, a_checkPoint
    a_checkPoint = True
    root.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("600x450+431+185")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="#d9d9d9")
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.name = tk.Label(
            self.Canvas1, background="#d9d9d9",  text='''Name''')
        self.name.place(relx=0.05, rely=0.178, height=20, width=40)

        self.Stock = tk.Label(
            self.Canvas1, background="#d9d9d9", text='''Stock''')
        self.Stock.place(relx=0.05, rely=0.289, height=20, width=40)

        self.price = tk.Label(
            self.Canvas1, background="#d9d9d9", text='''Price''')
        self.price.place(relx=0.6, rely=0.178, height=21, width=34)

        # Product Name Box
        self.a_name = ttk.Entry(self.Canvas1, cursor="ibeam")
        self.a_name.place(relx=0.133, rely=0.167,
                          relheight=0.067, relwidth=0.25)
        self.a_name.bind("<Tab>", self.price_focus)
        self.a_name.focus_set()

        # Product Price Box
        self.prev_price = tk.IntVar()

        self.a_price = ttk.Entry(
            self.Canvas1, cursor="ibeam", textvariable=self.prev_price)
        self.a_price.place(relx=0.683, rely=0.167,
                           relheight=0.067, relwidth=0.25)
        self.a_price.bind("<Tab>", self.focus_next_window)
        self.prev_price.set("")

        # Stock Spin Box
        self.stock_spin = tk.IntVar()

        self.a_stock = tk.Spinbox(self.Canvas1, from_=1, to=10000, background="white",
                                  buttonbackground="#d9d9d9", textvariable=self.stock_spin)
        self.a_stock.place(relx=0.133, rely=0.278,
                           relheight=0.067, relwidth=0.25)
        self.stock_spin.set('1')

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.a_tree = ScrolledTreeView(self.Canvas1)
        self.a_tree.place(relx=0.05, rely=0.444,
                          relheight=0.482, relwidth=0.717)

        self.a_tree.configure(columns="Col1 Col2 Col3")
        # build_treeview_support starting.
        self.a_tree.heading("#0", text="Product ID", anchor="center")
        self.a_tree.column("#0", width="65", minwidth="20",
                           stretch="1", anchor="center")

        self.a_tree.heading("Col1", text="Product", anchor="center")
        self.a_tree.column("Col1", width="65", minwidth="20",
                           stretch="1", anchor="center")

        self.a_tree.heading("Col2", text="Stock", anchor="center")
        self.a_tree.column("Col2", width="65",
                           minwidth="20", stretch="1", anchor="center")

        self.a_tree.heading("Col3", text="Unit Price", anchor="center")
        self.a_tree.column("Col3", width="65",
                           minwidth="20", stretch="1", anchor="center")

        self.product_show()

        # Add Button
        self.a_add_btn = tk.Button(
            self.Canvas1, background="#d9d9d9", text='''ADD''')
        self.a_add_btn.place(relx=0.808, rely=0.444, height=50, width=90)
        self.a_add_btn.bind('<Button-1>', lambda event,
                            entryField=self.a_name: self.product_add_btn(event, entryField))
        top.bind(
            "<Return>", lambda event, entryField=self.a_name: self.product_add_return(event, entryField))

        # Update Button
        self.a_update_btn = tk.Button(
            self.Canvas1, background="#d9d9d9", text='''UPDATE''')
        self.a_update_btn.place(relx=0.808, rely=0.622, height=50, width=90)
        self.a_update_btn.bind('<Button-1>', lambda event,
                               entryField=self.a_name: self.product_update_btn(event, entryField))
        # self.a_update_btn.bind("<Return>", lambda event,
        #                        entryField=self.a_name: self.product_update_return(event, entryField))

        # Delete Button
        self.a_del_btn = tk.Button(
            self.Canvas1, background="#d9d9d9", text='''DELETE''', command=self.product_delete)
        self.a_del_btn.place(relx=0.808, rely=0.800, height=50, width=90)

    def product_show(self):

        # Connecting DB
        conn = sqlite3.connect('ims.db')

        # Fetching Values from DB
        my_cursor = conn.execute("SELECT rowid,* FROM product")
        items = my_cursor.fetchall()

        self.item_names = []

        for item in items:
            self.a_tree.insert('', 'end', text=item[0], values=(
                item[1], item[2], item[3])),

            self.item_names.append(item[1])

        my_cursor.close()
        conn.close()

    def focus_next_window(self, event):

        event.widget.tk_focusNext().focus()

        return("break")

    def price_focus(self, event):

        try:
            name = str(self.a_name.get())

            conn = sqlite3.connect('ims.db')
            my_cursor = conn.execute(
                "SELECT rowid,* FROM product WHERE name=?", (name,))
            data_row = my_cursor.fetchone()

            price = data_row[3]

            stock = data_row[2]

            event.widget.tk_focusNext().focus()

            self.prev_price.set(price)

            self.stock_spin.set(stock)

            my_cursor.close()
            conn.close()

            return("break")

        except:

            event.widget.tk_focusNext().focus()

            return("break")

    def product_add_btn(self, event, entryField):

        if self.a_name.get() not in self.item_names:

            self.product_add()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror("Warning", "Product already exists.")

    def product_add_return(self, event, entryField):

        if self.a_name.get() not in self.item_names:

            self.product_add()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror("Warning", "Product already exists.")

    def product_add(self):

        conn = sqlite3.connect('ims.db')

        name = str(self.a_name.get())
        stock = float(self.a_stock.get())
        price = float(self.a_price.get())

        name = name.lower()

        try:

            my_cursor = conn.execute(
                "INSERT INTO product VALUES(?,?,?,?)", (name, stock, price, price))

            conn.commit()

            my_cursor = conn.execute(
                "SELECT rowid,* FROM product WHERE name=?", (name,))
            data_row = my_cursor.fetchone()

            self.a_tree.insert('', 'end', text=data_row[0], values=(
                data_row[1], data_row[2], data_row[3])),

            self.item_names.append(data_row[1])

            my_cursor.close()
            conn.close()

            # Clearing boxes
            self.stock_spin.set('1')
            self.a_name.delete(0, 'end')
            self.a_price.delete(0, 'end')

        except sqlite3.Error as my_err:
            print("error: ", my_err)

    def product_update_btn(self, event, entryField):

        if self.a_name.get() in self.item_names:

            self.product_update()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror(
                "Warning", "Product doesn't exists.\nPlease 'ADD' the product.")

    def product_update_return(self, event, entryField):

        if self.a_name.get() in self.item_names:

            self.product_update()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror(
                "Warning", "Product doesn't exists.\nPlease 'ADD' the product.")

    def product_update(self):

        conn = sqlite3.connect('ims.db')

        name = str(self.a_name.get())
        stock = float(self.a_stock.get())
        price = float(self.a_price.get())

        name = name.lower()

        every_item = self.a_tree.get_children()

        try:

            my_cursor = conn.execute(
                "UPDATE product SET name=?, stock=?, price=?, retail=? WHERE name=?", (name, stock, price, price, name))

            conn.commit()

            my_cursor = conn.execute(
                "SELECT rowid,* FROM product WHERE name=?", (name,))
            data_row = my_cursor.fetchone()

            my_cursor.close()
            conn.close()

            tree_items = []
            ids = []

            # getting names in tree view
            for i in self.a_tree.get_children():
                tree_items.append(self.a_tree.item(i)['values'][0])

            # Updating the considered item
            for i in range(len(tree_items)):
                if name != "" and name == tree_items[i][:len(name)]:
                    selections = tree_items[i]
                    indx = tree_items.index(selections)

            selected = every_item[indx]

            self.a_tree.item(selected, text=data_row[0], values=(
                data_row[1], data_row[2], data_row[3])),

            # Clearing boxes

            self.stock_spin.set('1')
            self.a_name.delete(0, 'end')
            self.a_price.delete(0, 'end')

        except sqlite3.Error as my_err:
            print("error: ", my_err)

    def product_delete(self):

        # selected item
        items = self.a_tree.selection()

        naam = self.a_tree.item(self.a_tree.selection())['values'][0]
        print(naam)

        conn = sqlite3.connect('ims.db')

        my_cursor = conn.execute("DELETE FROM product WHERE name=?", (naam,))

        conn.commit()

        self.a_tree.delete(items)

        # Show items after deleting

        my_cursor = conn.execute("SELECT rowid,* FROM product")
        items = my_cursor.fetchall()

        self.item_names = []

        print('Items after deletion:-')

        for item in items:
            self.item_names.append(item[1])
            print(item)

        my_cursor.close()
        conn.close()


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical',
                                command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @ staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind(
            '<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @ _create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>',
                       lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()