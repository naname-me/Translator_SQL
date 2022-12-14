from msilib.schema import ComboBox
from stat import FILE_ATTRIBUTE_NORMAL
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox
from Translator_SQL import *
def button_press():
    name_of_table = entry1.get()
    funct = entry2.get()
    name_of_colomn = entry3.get()
    if cb1Enabled !=0 :
        flag_where = True
        post_where = entry5.get()
        post_condition = entry6.get()
    else:
        flag_where = False
        post_where = '' 
        post_condition = ''
    if cb2Enabled != 0:
        flag_order_by = True
        post_order_by = entry7.get()
        if combx1.get()== "Возрастание":
            asc_desc = False
        else:
            asc_desc = True
    else:
        flag_order_by = False
        post_order_by = ''
        asc_desc = False
    if cb3Enabled != 0:
        flag_limit = True
        post_limit = entry8.get()
    else:
        flag_limit = False
        post_limit = ''
    if cb4Enabled.get() != 0:
        flag_uniq = True
    else:
        flag_uniq = False



    distinct=''
    result = requests_sql(name_of_table, funct, name_of_colomn, flag_uniq, distinct, flag_where, post_where, post_condition, flag_order_by, post_order_by, asc_desc, flag_limit, post_limit)
    entry4.delete(0, END)
    entry4.insert(0, result)

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 30
        y = y + cy + self.widget.winfo_rooty() +5
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("Courier New", "12", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def cb1foo():
    global label6,label7,entry6,entry5
    if cb1Enabled.get() != 0:
        label6['state']=ACTIVE
        label7['state']=ACTIVE
        entry6['state']=NORMAL
        entry5['state']=NORMAL
    else:
        label6['state']=DISABLED
        label7['state']=DISABLED
        entry6['state']=DISABLED
        entry5['state']=DISABLED
def cb2foo():
    global label8,label9,entry7,combx1
    if cb2Enabled.get() != 0:
        label9['state']=ACTIVE
        label8['state']=ACTIVE
        entry7['state']=NORMAL
        combx1['state']=NORMAL
    else:
        label9['state']=DISABLED
        label8['state']=DISABLED
        entry7['state']=DISABLED
        combx1['state']=DISABLED
def cb3foo():
    global label10,entry8
    if cb3Enabled.get() != 0:
        label10['state']=ACTIVE
        entry8['state']=NORMAL
    else:
        label10['state']=DISABLED
        entry8['state']=DISABLED
def cb4foo():
    return 0
    
SIZET = 14





window = Tk()
window.title("")
#window.resizable(width=False, height=False)
window.geometry("970x440")
window.iconbitmap()
label1 = Label(
    text="Переводчик с естественного языка на SQL",
    fg="white",
    bg="black", 
    width=90, 
    height=2,
    font=('Courier New',14))
label1.pack()

label2 = Label(text="Введите название таблицы:",font=('Courier New',SIZET))
label2.place(x=20, y=50)
entry1 = Entry(width=25,font=('Courier New',SIZET))
entry1.place(x=20, y=80)

label3 = Label(text="Введите агрегаторную функцию:",font=('Courier New',SIZET))
label3.place(x=330,y=50)
entry2 = Entry(width=25,font=('Courier New',SIZET))
entry2.place(x=330,y=80)

label4 = Label(text="Введите имя столбца:",font=('Courier New',SIZET))
label4.place(x=670,y=50)
entry3 = Entry(width=25,font=('Courier New',SIZET))
entry3.place(x=670,y=80)


cb1Enabled = IntVar()
cb1 = Checkbutton(text="Есть ли условие?", font=('Courier New',SIZET), variable=cb1Enabled, command=cb1foo)
cb1.place(x=20,y=150)
label6 = Label(text="Введите имя столбца:",font=('Courier New',SIZET),state=DISABLED)
label6.place(x=330,y=120)
entry5 = Entry(width=25,font=('Courier New',SIZET),state=DISABLED)
entry5.place(x=330,y=150)
label7 = Label(text="Введите условие:",font=('Courier New',SIZET),state=DISABLED)
label7.place(x=670,y=120)
entry6 = Entry(width=25,font=('Courier New',SIZET),state=DISABLED)
entry6.place(x=670,y=150)

cb2Enabled = IntVar()
cb2 = Checkbutton(text="Есть ли сортировка?", font=('Courier New',SIZET), variable=cb2Enabled, command=cb2foo)
cb2.place(x=20,y=220)
label8 = Label(text="Введите имя столбца:",font=('Courier New',SIZET), state=DISABLED)
label8.place(x=330,y=190)
entry7 = Entry(width=25,font=('Courier New',SIZET), state=DISABLED)
entry7.place(x=330,y=220)
label9 = Label(text="Убывание/Возрастание:",font=('Courier New',SIZET), state=DISABLED)
label9.place(x=670,y=190)
combox1Values = ["Убывание", "Возрастание"]
combx1 = Combobox(values = combox1Values, state=DISABLED) #combobox.get()
combx1.place(x=670,y=220)

cb3Enabled = IntVar()
cb3 = Checkbutton(text="Есть ли лимит вывода?", font=('Courier New',SIZET), variable=cb3Enabled, command=cb3foo)
cb3.place(x=20,y=290)
label10 = Label(text="Введите лимит:",font=('Courier New',SIZET), state=DISABLED)
label10.place(x=330,y=260)
entry8 = Entry(width=25,font=('Courier New',SIZET), state=DISABLED)
entry8.place(x=330,y=290)

cb4Enabled = IntVar()
cb4 = Checkbutton(variable=cb4Enabled, command=cb4foo)
cb4.place(x=950,y=80)
CreateToolTip(cb4,text = "Уникальность записей")


button1 = Button(
    text="Получить результат",
    bg="black",
    fg="white",
    command=button_press,
    font=('Courier New',SIZET))
button1.place(x=20,y=360)

label5 = Label(text="Результат:",font=('Courier New',SIZET))
label5.place(x=330,y=340)
entry4 = Entry(width=55,font=('Courier New',SIZET))
entry4.place(x=330,y=370)

window.mainloop()
