import tkinter
import codecs
from tkinter import *
from tkinter.filedialog import askopenfilenames, asksaveasfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from settings import *

class Text_editor():
    def __init__(self):
        self.filename = tkinter.NONE

    def new_file(self):
        self.file_name = 'Без названия'   
        text.delete('1.0', tkinter.END)

    def open_file(self):
        inp =  askopenfilename()
        if inp == '':
            return 
        with codecs.open(inp, encoding='utf-8') as f:    
            data = f.read()
            text.delete('1.0', tkinter.END)
            text.insert('1.0', data)       

    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode='w', defaultextension='txt')
        data = text.get('1.0', tkinter.END)  
        try: 
            output.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка!', message='Ошибка при сохранении файла')    

    def get_info(self):
        messagebox.showinfo('Справка', "Информация о нашем приложении! Спасибо что его используете :)")        
