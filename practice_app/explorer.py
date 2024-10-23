import tkinter
import os
import pprint
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    # text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)


def tell_about():
    filename = 'about.txt'
    file = open(filename, mode='r', encoding='utf-8')
    text2['text'] = file.read()
    file.close()
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('500x200')
window.configure(bg='grey')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', height=3, width=20, background='silver')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', command=file_select)
button_select.grid(column=1, row=2, pady=5)
button_select.configure(bg='yellow', fg='green')
text2 = tkinter.Label(window, text='О программе', height=3, width=20, background='silver')
text2.grid(column=2, row=1)
button_about = tkinter.Button(window, width=20, height=3, text='Информация', foreground='green',
                              background='yellow', command=tell_about)
button_about.grid(column=2, row=2, pady=5)

window.mainloop()
