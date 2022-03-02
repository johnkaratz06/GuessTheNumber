from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import random
from tkinter import messagebox
window = Tk()
window.title("Quiz")
window.geometry('500x350')



def check(*args):
    global tries
    lbl7.place_forget()
    lbl10.config(text="", foreground="red")
    y=txt2.get()
    if y.isdecimal()==False:
        lbl10.config(text="ONLY NUMBERS PLEASE")
    elif int(y)<0:
        lbl10.config(text="ONLY NUMBERS ABOVE 0")
    elif choice==1 and int(y)>20:
        lbl10.config(text="ONLY NUMBERS BELOW 20 (SELECTED)")
    elif choice==2 and int(y)>50:
        lbl10.config(text="ONLY NUMBERS BELOW 50 (SELECTED)")
    elif choice==3 and int(y)>100:
        lbl10.config(text="ONLY NUMBERS BELOW 100 (MAX)")
    elif x<int(txt2.get()):
        txt2.config(state="disabled")
        lbl8.place_forget()
        lbl9.place(x=275, y=175)
        window.update()
        window.after(1500)
        lbl9.place_forget()
        lbl6.place(x=275, y=175)
        txt2.config(state="enabled")
        txt2.delete(0, END)
        tries += 1
        lbl11.config(text="Tries: "+str(tries))
    elif x>int(txt2.get()):
        txt2.config(state="disabled")
        lbl6.place_forget()
        lbl9.place(x=275, y=175)
        window.update()
        window.after(1500)
        lbl9.place_forget()
        lbl8.place(x=275, y=175)
        txt2.config(state="enabled")
        txt2.delete(0, END)
        tries += 1
        lbl11.config(text="Tries: " + str(tries))
    else:
        lbl8.place_forget()
        lbl6.place_forget()
        lbl7.place(x=275, y=175)
        txt2.config(state="disabled")
        tries += 1
        lbl11.config(text="Tries: " + str(tries))
    if tries<3: lbl11.config(foreground="green")
    elif tries<5: lbl11.config(foreground="orange")
    else: lbl11.config(foreground="red")
    window.bind("<Return>", check)
    window.bind("<B1-Motion>",check2)

def check2(*args):
    if rb2!=rb:
        rb2.set(rb)
        lbl10.config(text="CHANGE AFFECTS NEXT ROUND")

def ran():
    global x
    global tries
    global choice
    tries = 0
    lbl11.config(text="Tries: " + str(tries),foreground="green")
    rad1.config(state="disabled")
    rad2.config(state="disabled")
    rad3.config(state="disabled")
    lbl6.place_forget()
    lbl7.place_forget()
    lbl8.place_forget()
    lbl9.place_forget()
    lbl10.config(text="",foreground="red")
    txt2.config(state="enabled")
    txt2.delete(0, END)
    txt2.config(state="disabled")
    btn1.config(state="disabled")
    btn3.config(state="disabled")
    lbl5.place(x=275, y=175)
    for i in range(0,3):
        lbl4.config(text=".")
        window.after(500)
        window.update()
        lbl4.config(text="..")
        window.after(500)
        window.update()
        lbl4.config(text="...")
        window.after(500)
        window.update()
    choice = rb.get()
    if choice==1: x=random.randint(0,20)
    elif choice==2: x=random.randint(0,50)
    else: x=random.randint(0,100)
    print(x)
    txt2.config(state="enabled")
    lbl4.config(text="")
    rad1.config(state="enabled")
    rad2.config(state="enabled")
    rad3.config(state="enabled")
    btn1.config(state="enabled")
    btn3.config(state="enabled")
    lbl10.config(text=">>Your number is ready!", foreground="green")
    window.bind("<Return>",check)
def clos():
    y=str(txt2.get())
    exitmsg = messagebox.askyesno("ALERT","Are you sure you want to exit?")
    if exitmsg:
        if x==0:
            messagebox.showinfo("ALERT", "Goodbye!")
        elif str(x)==y:
            messagebox.showinfo("ALERT", "You got it right!\nYour tries: " + str(tries))
        else:
            messagebox.showinfo("ALERT", "The number was: " + str(x) + "\nYour tries: " + str(tries))
        window.destroy()
def start(*args):
    lbl10.config(text="",foreground="")
    if txt2.get()!="":
        global x
        global rb2
        global rb
        global rad1
        global rad2
        global rad3
        lbl10.config(text=">>Welcome player " + str(txt2.get())+"!")
        txt2.delete(0, END)
        global rb
        lbl2.destroy()
        lbl1.destroy()
        btn.destroy()
        lbl0.place(x=20,y=20)
        txt2.place(x=30,y=173)
        txt2.config(width=10,state="disabled")
        lbl3.place(x=20,y=87)
        btn3.place(x=170,y=85)
        lbl11.place(x=370,y=20)
        x=0
        rb = IntVar()
        rb.set(2)
        rb2 = IntVar()
        rb2.set(rb)
        rad1 = Radiobutton(window, text="EASY(0-20)", value=1, variable=rb,style="My.TRadiobutton")
        rad1.place(x=30,y=120)
        rad2 = Radiobutton(window, text="MEDIUM(0-50)", value=2, variable=rb,style="My.TRadiobutton")
        rad2.place(x=150,y=120)
        rad3 = Radiobutton(window, text="HARD(0-100)", value=3, variable=rb,style="My.TRadiobutton")
        rad3.place(x=290,y=120)
        btn1.place(x=65,y=220)
        btn2.place(x=65,y=250)
        lbl4.place(x=100,y=280)
    else:
        lbl10.config(text=">>PLEASE FILL IN YOUR NAME",foreground="red")

def ranfordif():
    choice=random.randint(1,3)
    rb.set(choice)

style0 = Style(window)
style0.configure("My.TLabel", font=('Segoe UI',25))
style1 = Style(window)
style1.configure("My.TButton", font=(25))
style2 = Style(window)
style2.configure("My.TRadiobutton", font=(20))
lbl0 = Label(window,text=" GUESS THE NUMBER ",style="My.TLabel",borderwidth=20,relief="groove")
lbl0.pack()
lbl1 = Label(window,text="HELP: Write in the box the\nnumber you think it might be!\nusername:",style="My.TLabel",justify=CENTER)
lbl1.pack()
txt2 = Entry(window,font=("Helvetica",25),justify=CENTER)
txt2.pack()
btn = Button(window,text="START",style="My.TButton",command=start)
btn.pack()
lbl2 = Label(window,font=("Helvetica",10))
lbl2.pack()
lbl3 = Label(window,text="DIFFICULTY:",font=("Helvetica",15))
btn1 = Button(window,text="RANDOMIZE",style="My.TButton",command=ran)
btn2 = Button(window,text="CLOSE",style="My.TButton",command=clos)
lbl4 = Label(window,style="My.TLabel")

imgimp1 = Image.open("guessnum\die.png").resize((128, 128), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(imgimp1)
lbl5 = Label(window,image=img1)
imgimp2 = Image.open("guessnum\down.png").resize((128, 128), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(imgimp2)
lbl6 = Label(window,image=img2)
imgimp3 = Image.open("guessnum\dt.png").resize((128, 128), Image.ANTIALIAS)#tick
img3 = ImageTk.PhotoImage(imgimp3)
lbl7 = Label(window,image=img3)
imgimp4 = Image.open("guessnum\drrow.png").resize((128, 128), Image.ANTIALIAS)#up
img4 = ImageTk.PhotoImage(imgimp4)
lbl8 = Label(window,image=img4)
imgimp5 = Image.open("guessnum\dx.png").resize((128, 128), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(imgimp5)
lbl9 = Label(window,image=img5)

lbl10 = Label(window,font=(10))
lbl10.place(x=20,y=300)
tries = 0
lbl11 = Label(window,text="Tries: "+str(tries),font=("Segoe UI",20))

btn3 = Button(window,text="RANDOM",style="My.TButton",command=ranfordif)
window.bind("<Return>",start)
window.mainloop()