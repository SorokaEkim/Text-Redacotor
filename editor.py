from module import *

app = tkinter.Tk() 
app.title(APP_NAME)
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)


text = tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap='word')
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview)  
scroll.pack(side='right', fill='y')
text.configure(yscrollcommand=scroll.set)
text.pack()

menuBar = tkinter.Menu(app)

editor = Text_editor()

app_menu = tkinter.Menu(menuBar)
app_menu.add_command(label='Новый', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)


menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Справка')
menuBar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menuBar)

app.mainloop()