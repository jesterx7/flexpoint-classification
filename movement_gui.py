from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import csv

def update_data(filepath):
	with open(filepath, newline='') as f:
		reader = csv.reader(f)
		data = list(reader)

	trv.delete(*trv.get_children())
	for val in data:
		trv.insert('', 'end', values=val)

def read_data():
	filepath = str(entry.get()) + ".csv"
	update_data(filepath)

win = Tk()
wrapper_widget = LabelFrame(win, text="Action")
wrapper_data = LabelFrame(win, text="Data")

wrapper_widget.pack(fill="both", padx=10, pady=10)
wrapper_data.pack(fill="both", expand="yes", padx=10, pady=10)
t_head = [i for i in range(17)]
head_name = [
        '', 'pinky MCP', 'pinky PIP', 'ring MCP', 'ring PIP', 'middle MCP', 'middle PIP', 'index MCP', 'index PIP',
        'thumb MCP', 'thumb PIP', 'Accelerometer X', 'Accelerometer Y', 'Accelerometer Z', 'Magenetometer X',
        'Magenetometer Y', 'Magenetometer Z'
    ]

trv = ttk.Treeview(wrapper_data, columns=(t_head))
style = ttk.Style(trv)
style.configure('Treeview', rowheight=40)

trv.pack(side=LEFT)
trv.place(x=0, y=0)

for i in range(17):
	if (i == 0):
		trv.column('#'+str(i), anchor="center", width=30, minwidth=30)
		continue
	trv.heading('#'+str(i), text=head_name[i])
	trv.column('#'+str(i), anchor="center", width=33, minwidth=150)

yscrollbar = ttk.Scrollbar(wrapper_data, orient="vertical", command=trv.yview)
yscrollbar.pack(side=RIGHT, fill="y")

xscrollbar = ttk.Scrollbar(wrapper_data, orient="horizontal", command=trv.xview)
xscrollbar.pack(side=BOTTOM, fill="x")

logo = ImageTk.PhotoImage(Image.open("Logo/flexpoint.png"))
label_logo = Label(wrapper_widget, image=logo)
label_logo.pack(side=TOP, padx=10)

label_search = Label(wrapper_widget, text="Masukkan nama file ", anchor="w")
label_search.pack(fill="x")

entry = Entry(wrapper_widget, textvariable='file')
entry.pack(fill="x", padx=5)

button_read = Button(wrapper_widget, text="Read", command=read_data, anchor="n")
button_read.pack(side=LEFT, fill="x", padx=5, pady=5)

record_read = Button(wrapper_widget, text="Record", anchor="n")
record_read.pack(side=LEFT, fill="x", padx=5, pady=10)

trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

update_data('1_1.csv')

win.geometry("800x600")
win.resizable(False, False)
win.title("Flexpoint")
win.mainloop()