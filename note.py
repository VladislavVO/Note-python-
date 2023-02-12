import tkinter as tk
from tkinter import filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('800x600')
main_application.title('Notepad')
main_menu = tk.Menu()

file = tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label='File',menu=file)

text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand= scroll_bar.set)

current_font_family= 'Arial'
current_font_size= 11

def clear_file():
    global url 
    url = ''
    text_editor.delete(1.0,tk.END)

file.add_command(label='Clear', compound=tk.LEFT, command=clear_file )


def open_file():
    global url
    url = filedialog.askopenfilename(initialdir= os.getcwd(), title ='Select File',filetypes=(('CSV File','*.csv'),('All files','*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return 
    except :
        return
    main_application.title(os.path.basename(url))

file.add_command(label='Open', compound=tk.LEFT,command =open_file )


def save_file():
    global url
    try:
        if url :
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding= 'utf-8') as fw:
                fw.write(content)
        else :
            url = filedialog.asksaveasfile(mode = 'w' ,defaultextension = '.csv',filetypes=(('CSV File','*.csv'),('All files','*.*')))
            content = text_editor.get(1.0,tk.END)
            url.write(content)
            url.close()
    except :
        return 

file.add_command(label='Save', compound=tk.LEFT, command= save_file )


def save_as():
    global url
    try :
        content=text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w' ,defaultextension = '.csv',filetypes=(('CSV File','*.csv'),('All files','*.*')))
        url.write(content)
        url.close
    except :
        return

file.add_command(label='Save As', compound=tk.LEFT, command =save_as )

text_changed = True

def changed():
    global text_changed
    if text_editor.edit_modified():
        text_changed= True
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)

def exit_func():
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file')
            if mbox is True :
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w' ,defaultextension = '.csv',filetypes=(('CSV File','*.csv'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 

file.add_command(label='Exit', compound=tk.LEFT, command=exit_func )

main_application.config(menu=main_menu)
main_application.mainloop()
