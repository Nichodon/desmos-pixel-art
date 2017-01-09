from Tkinter import *

colors = ['#c74440', '#fa7e19', '#388c46', '#2d70b3', '#6042a6', 'black', 'white']
outlines = ['#c74440', '#fa7e19', '#388c46', '#2d70b3', '#6042a6', 'black', 'black']
hovers = ['#e3a2a0', '#fdbf8c', '#9cc6a3', '#96b8d9', '#b0a1d3', '#808080', '#b3b3b3']
current = 6

order = [0, 3, 2, 1, 4, 5]

canvasses = []
types = []
outputs = []
buttons = []

tk = Tk()
tk.wm_title('Desmos Pixel Art Generator')

f4 = LabelFrame(tk, relief=FLAT, padx=10, pady=10)
f4.grid(row=0, column=0)


def generate():
    output = []
    for x in range(6):
        a_list = []
        for y in range(2):
            a_list.append('')
        output.append(a_list)
    for x in range(len(canvasses)):
        for y in range(len(canvasses[0])):
            if types[x][y] < 6:
                output[types[x][y]][0] += str(y) + ','
                output[types[x][y]][1] += str(-x + 19) + ','
    for x in range(6):
        output[x][0] = output[x][0][:-1]
        output[x][1] = output[x][1][:-1]
        outputs[order[x]].config(state='normal')
        outputs[order[x]].delete(1.0, END)
        outputs[order[x]].insert(END, '([' + output[x][0] + '],[' + output[x][1] + '])')
        outputs[order[x]].config(state='disabled')


def clear():
    for x in range(len(canvasses)):
        for y in range(len(canvasses[0])):
            canvasses[x][y].config(bg='white')
            types[x][y] = 6


def change(event):
    global current
    item = event.widget.find_closest(event.x, event.y)[0]
    tags = event.widget.gettags(item)
    current = int(tags[0])


def color(event):
    event.widget.config(bg=colors[current])
    item = event.widget.find_closest(event.x, event.y)[0]
    tags = event.widget.gettags(item)
    types[int(tags[0].split(',')[0])][int(tags[0].split(',')[1])] = current

f1 = LabelFrame(f4, text='Canvas', padx=10, pady=10)
f1.grid(row=0, column=0)

for i in range(32):
    array = []
    empty = []
    for j in range(32):
        c = Canvas(f1, bg='white', width=16, height=16, highlightthickness=1)
        c.create_oval(1, 1, 20, 20, fill='', outline='', tags=str(i) + ',' + str(j))
        c.grid(row=i, column=j)
        c.bind('<Button-1>', color)
        array.append(c)
        empty.append(6)
    canvasses.append(array)
    types.append(empty)

f2 = LabelFrame(f4, relief=FLAT, pady=10)
f2.grid(row=1, column=0)

for i in range(7):
    c = Canvas(f2, width=20, height=20)
    c.create_oval(2, 2, 21, 21, fill=colors[i], activefill=hovers[i], outline=outlines[i], tags=str(i))
    c.grid(row=0, column=i)
    c.bind('<Button-1>', change)
    buttons.append(c)

f3 = LabelFrame(f4, relief=FLAT)
f3.grid(row=2, column=0)

b1 = Button(f3, text='Clear Canvas', command=clear)
b1.grid(row=0, column=0, padx=5)

b2 = Button(f3, text='Generate Code', command=generate)
b2.grid(row=0, column=1, padx=5)

f5 = LabelFrame(f4, text='Output', padx=10, pady=10)
f5.grid(row=3, column=0)

f6 = Frame(f5, width=576, height=130)
f6.grid(row=0, column=0)
f6.columnconfigure(0, weight=10)
f6.grid_propagate(False)

for i in range(6):
    t = Text(f6, bg='white', height=1, bd=0)
    t.config(state='disabled')
    t.insert(END, 'hi')
    t.grid(row=i, column=0, sticky='we', pady=2)
    outputs.append(t)

mainloop()
