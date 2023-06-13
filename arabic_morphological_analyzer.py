# Import Libraries
import tkinter as tk
from tkinter import ttk
import Program as pg
import loading_screen as ld
import ArabicPluralDetector as fb


def Home():
    for widget in root.winfo_children():
        widget.place_forget()
    canvas.itemconfig(text, text="Morographical Analysis")
    
    about_btn.place(x=200,y=450)
    typ_btn.place(x=350,y=500)
    enter_btn.place(x=350,y=450)
    exit_btn.place(x=500,y=450)
    
    home_btn.place_forget()
    text_input.place_forget()
    gen_btn.place_forget()
    generate_btn.place_forget()
    

def About():
    canvas.itemconfig(text, text="")
    label0 = tk.Label(root, text=("د/عزة طه") ,font=("italic"))
    label0.config(width=30)
    label0.place(x=250,y=140)
    label1 = tk.Label(root, text=("يوسف محمد سعيد") ,font=("Arial"))
    label1.config(width=30)
    label1.place(x=250,y=200)
    label2 = tk.Label(root, text=("أحمد خالد محمد كامل") ,font=("Arial"))
    label2.config(width=30)
    label2.place(x=250,y=260)
    label3 = tk.Label(root, text=("محمد عبدالوهاب") ,font=("Arial"))
    label3.config(width=30)
    label3.place(x=250,y=320)
    label4 = tk.Label(root, text=("أحمد محمد محمود") ,font=("Arial"))
    label4.config(width=30)
    label4.place(x=250,y=380)

    home_btn.place(x=350,y=450)
    
    
    about_btn.place_forget()
    typ_btn.place_forget()
    enter_btn.place_forget()
    exit_btn.place_forget()
 
    
def Typ():
        canvas.itemconfig(text, text="")
    
        text_input.place(x=220,y=40)
        gen_btn.place(x=80,y=37)
        home_btn.place(x=80,y=500)
    
        about_btn.place_forget()
        enter_btn.place_forget()
        typ_btn.place_forget()
        exit_btn.place_forget()
        

def Enter():
    canvas.itemconfig(text, text="")
    
    text_input.place(x=220,y=40)
    generate_btn.place(x=80,y=37)
    home_btn.place(x=80,y=500)

    about_btn.place_forget()
    enter_btn.place_forget()
    typ_btn.place_forget()
    exit_btn.place_forget()
    
    
def Gen():
    for widget in root.winfo_children():
        widget.place_forget()
    text_input.place(x=220, y=40)
    gen_btn.place(x=80, y=37)
    home_btn.place(x=80, y=500)

    input_text = text_input.get()

    detector = fb.ArabicPluralDetector()

    words = input_text.split()
    num_words = len(words)

    header = tk.Label(root, text='word')
    header.config(width=18)
    header.place(x=400, y=150)
    header = tk.Label(root, text='type')
    header.config(width=18)
    header.place(x=300, y=150)

    m = 0
    n = 0
    r = 0
    for i in range(num_words):
        header = tk.Label(root, text=words[i])
        header.config(width=18)
        header.place(x=400, y=173+m)

        output = detector.detect_plural(words[i])
        num_outputs = len(output)

        n = 0
        for j in range(num_outputs):
            cell = tk.Label(root, text=output[j])
            cell.config(width=18)
            cell.place(x=300-n, y=173+r)  
            
        n = 0
        r += 23
        m += 23


def Generate():
    for widget in root.winfo_children():
        widget.place_forget()
    text_input.place(x=220, y=40)
    generate_btn.place(x=80, y=37)
    home_btn.place(x=80, y=500)

    input_text = text_input.get()
    words,outputs = pg.program.run(input_text)
    columns = len(input_text.split())
    m = 0
    n = 0
    r = 0
    
    header = tk.Label(root, text='word')
    header.config(width=10)
    header.place(x=400,y=150)
    header = tk.Label(root, text='root')
    header.config(width=10)
    header.place(x=320,y=150)
    for i in range(0,columns):
        header = tk.Label(root, text=words[i])
        header.config(width=10)
        header.place(x=400,y=173+m)
        for w in outputs[i]:
            n += 70
            cell = tk.Label(root, text=w)
            cell.config(width=10)
            cell.place(x=390-n,y=173+r)
        n = 0
        r += 23
        m += 23

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")


root = tk.Tk()
root.title("Morographical Analysis")
root.overrideredirect(True)  
center_window(root, 800, 600)


canvas = tk.Canvas(root, width=800, height=700,background="#669CB2")
canvas.pack()

text = canvas.create_text(-200, 100, text="Morographical Analysis", font=("Arial", 20),fill="#000000")

about_btn = ttk.Button(root, text="About", style="MyButton.TButton" , command=About)
about_btn.place(x=150,y=350)

enter_btn = ttk.Button(root, text="Enter", style="MyButton.TButton",command=Enter)
enter_btn.place(x=250,y=350)

typ_btn = ttk.Button(root, text="Type", style="MyButton.TButton",command=Typ)
typ_btn.place(x=350,y=350)


def distroy():
    root.destroy()


exit_btn = ttk.Button(root, text="Exit", style="MyButton.TButton", command=distroy)
exit_btn.place(x=350,y=350)

home_btn = ttk.Button(root, text="Home", style="MyButton.TButton", command=Home)
home_btn.place(x=250,y=350)

def on_entry_click(event):        
    text_input.delete(0, "end") 
    text_input.insert(0, '') 
    text_input.config(fg = 'black')
def leave_entry_click(event):        
    if text_input.get() == "":
        text_input.insert(0, '...ادخل الجملة') 
        text_input.config(fg = 'black')
entry_text = tk.StringVar(value='...ادخل الجملة')
text_input = tk.Entry(root ,validate='key', width=60 ,textvariable=entry_text,justify='right')
text_input.bind('<FocusIn>', on_entry_click)
text_input.bind('<FocusOut>', leave_entry_click)

gen_btn = ttk.Button(root, text="Generate", style="MyButton.TButton", command=Gen)


generate_btn = ttk.Button(root, text="Generate", style="MyButton.TButton", command=Generate)


def animate():
    canvas.move(text,8,0)
    if canvas.coords(text)[0] > 800:
        canvas.coords(text, -200, 100)
    root.after(50, animate)

Home()
animate()

root.mainloop()
