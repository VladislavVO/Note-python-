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

main_application.config(menu=main_menu)
main_application.mainloop()