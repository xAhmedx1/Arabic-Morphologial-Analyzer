from tkinter import *
from tkinter.ttk import Progressbar
import sys, os

dir_path = os.path.join(sys.path[0])

root = Tk()
root.resizable(0, 0)
height = 700
width = 800
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.wm_attributes('-topmost', True)

root.overrideredirect(1)
root.config(background='#669CB2')

exit_btn = Button(root, text='X', command=lambda: exit_window(), font=("yu gothic ui", 13, 'bold'), fg='green', bg='#669CB2', bd=0, activebackground='#669CB2')
exit_btn.place(x=770, y=0)

welcome_label = Label(root, text='Morographical Analysis', font=("yu gothic ui", 19, 'bold'), bg='#669CB2')
welcome_label.place(x=250, y=15)




image = PhotoImage(file=os.path.join(dir_path, 'gg.png'))
# image = PhotoImage(file='gg.png')
bg_label = Label(root, bg='#669CB2')
bg_label.place(x=150, y=65)
progress_label = Label(root, text='please wait...', font=("yu gothic ui", 13, 'bold'), bg='#669CB2')
progress_label.place(x=320, y=520)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=120, y=550)
def exit_window():
    sys.exit(root.destroy())




i = 0
def load():
    global i
    if i <= 10:
        txt = 'please wait...' +(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(100, load)
        progress['value'] = 10*i
        i += 1
    if progress['value'] == 100:
        root.destroy()
load()

root.mainloop()

