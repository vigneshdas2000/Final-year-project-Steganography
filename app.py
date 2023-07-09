from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
from ImageSteg import ImageSteg
import os
import ast
import pandas as pd
import numpy as np
import random
from numpy.core.arrayprint import printoptions

global LSB
LSB=ImageSteg()

#python -m PyInstaller ./app.py --onefile --windowed

#---------------------------------------------------------------
def signin():
    global username
    global password
    global logo
    username=user.get()
    password=code.get()
    file=open('asset/datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    if username in r.keys() and password==r[username]:
#Selection Window---------------------------------------------
        global mid
        messagebox.showinfo("Success","Login Successfull")
        root.destroy()
        mid=Tk()
        mid.title("Secrecy - Hide secret text message in image")
        #mid.geometry("720x600+400+100")
        mid.geometry('925x500+300+200')
        mid.configure(bg="white")
        mid.resizable(False, False)
       
       #icon
        image_icon=PhotoImage(file="asset/logon.png")
        mid.iconphoto(False,image_icon)
       
       #logo
        logo=PhotoImage(file="asset/select.png")
        Label(mid,image=logo,bg="white").place(x=20,y=130)
        
        frame=Frame(mid, width=500,height=350, bg="white")
        frame.place(x=420,y=70)
        heading=Label(frame, text='Select From The Given Options', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=0,y=5)
       #Encode button
        frame_1=Frame(mid,bg="white",width=400,height=80,relief=GROOVE)
        frame_1.place(x=470,y=150)

        Button(frame_1,bd=6,bg='#084e9c',fg='white',activebackground = "white",text="Encode",width=8,height=1,font=('Microsoft YaHei UI Light', 12, 'bold'),relief=RAISED,command=encode).place(x=110,y=35)
        Label(frame_1,text="To Encode Your Message In The Image",fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=35,y=5)

       #Decode button
        frame_2=Frame(mid,bg="white",width=400,height=80,relief=GROOVE)
        frame_2.place(x=470,y=250)

        Button(frame_2,bd=6,bg='#084e9c',fg='white',activebackground = "white",text="Decode",width=8,height=1,font=('Microsoft YaHei UI Light', 12, 'bold'),relief=RAISED,command=decode).place(x=110,y=35)
        Label(frame_2,text="To Decode Your Message From The Image",fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=35,y=5)
       
       #Exit button
        def esc():
            answer = messagebox.askquestion("Exit Application", "Do you really want to exit?")
            if answer=='yes':
                mid.destroy()
                
        frame_3=Frame(mid,bg="white",width=400,height=80,relief=GROOVE)
        frame_3.place(x=470,y=350)
        
        Button(frame_3,width=10,pady=7,text='Exit',bg='#57a1f8',fg='white',border=0,command=esc).place(x=120,y=35)
        #Selection window closes----------------------------------------
    else:
        messagebox.showerror('Invalid','Invalid Username or Password')

#signup window starts----------------------------------------------------
def signup_command():
    root.destroy()
    window=Tk()
    window.title("SignUp")
    window.geometry ('925x500+300+200')
    window.configure (bg='#fff')
    window.resizable (False, False)
    image_icon=PhotoImage(file="asset/logo.jpg")
    window.iconphoto(False,image_icon)

    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()
    
        if password==confirm_password:
            try:
                file=open('asset/datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)
            
                dict2={username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()
    
                file=open('asset/datasheet.txt','w')
                w=file.write(str(r))
                file.close()
            
                messagebox.showinfo('Signup','Sucessfully sign up')
                window.destroy()
                main_screen()
            except:
                file=open('asset/datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid',"Both Password should match")
#-----------------------------------------------------------------
    def sign():
        window.destroy()
        main_screen()
#-----------------------------------------------------------------

    img=PhotoImage(file="asset/signup.png")
    Label(window,image=img, border=0, bg='white').place (x=50,y=90)

    frame=Frame(window, width=350,height=390, bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame, text='Sign up', fg="#57a1f8", bg='white', font = ('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100,y=5)
#-----------------------------------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')
        
    user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place (x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame (frame, width=295,height=2, bg='black').place(x=25,y=107)

#-----------------------------------------------------------------
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')
        
    code=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place (x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)

    Frame (frame, width=295,height=2, bg='black').place(x=25,y=177)

#-----------------------------------------------------------------
    def on_enter(e):
        confirm_code.delete(0,'end')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'Confirm Password')
        
    confirm_code=Entry(frame, width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_code.place (x=30,y=220)
    confirm_code.insert(0,'Confirm Password')
    confirm_code.bind("<FocusIn>",on_enter)
    confirm_code.bind("<FocusOut>",on_leave)

    Frame(frame, width=295,height=2, bg='black').place(x=25,y=247)
#-----------------------------------------------------------------
    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,y=280)

    label=Label (frame, text='I have an account', fg='black', bg='white', font = ('Microsoft YaHei UI Light',9))
    label.place (x=90,y=340)

    signin=Button (frame,width=6, text='Sign in', border=0, bg='white', cursor= 'hand2', fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)

    window.mainloop()
#end of signup--------------------------------------------------



#Encode Window Starts------------------------------------------
flag=0
f=0
secret=""
w=""
def encode():
    global logo
    mid.destroy()
    enc=Tk()
    enc.title("Secrecy - Hide secret text message in image")
    enc.geometry('925x600+300+200')
    enc.configure(bg="#57a1f8")
    enc.resizable(False, False)
    
    def showimage():
        global flag
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPEG File","*.jpeg"),
                                                   ("JPG file","*.jpg")))
        img=Image.open(filename)
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img,width=250,height=250)
        lbl.image=img
        flag=1

    def Hide():
        global secret
        global f
        global w
        message=text1.get("1.0","end-1c")

        if message =="":
            messagebox.showerror("Invalid","Enter your message")
            encode()
            
        for i in message:
            if i.isalnum() or i in [".",","," "]:
                str1= message
            else:
                messagebox.showerror("Invalid","Special characters not allowed in message")
                text1.delete("1.0","end-1c")
                encode()

        w=text2.get("1.0","end-1c")
        if len(w) == 5:
            watermark= w
        else:
            messagebox.showerror("Invalid","Invalid Watermark!")
            text2.delete("1.0","end-1c")
            encode()

        if flag ==0:
            messagebox.showerror("Invalid","Cover Image not selected")
            encode()

        messagebox.showinfo("Success","Message Encoded Successfully,Now You Can Save The Image")
        str2=LSB.encrypt(str1,watermark)
        secret=LSB.hide(str(filename),str2)

    def esc():
        answer = messagebox.askquestion("Exit Application", "Do you really want to exit?")
        if answer=='yes':
           enc.destroy()

    def save():
        if secret=="" or flag==0 or w=="":
            messagebox.showerror("Error","Click on Encode Button before saving!")
            encode()
            
        messagebox.showinfo("Saved","Encoded Image Saved In hidden Folder")
        secret.save("hidden/encrypted.png")

    #icon
    image_icon=PhotoImage(file="asset/logon.png")
    enc.iconphoto(False,image_icon)

    #logo
    logo=PhotoImage(file="asset/logo.png")
    Label(enc,image=logo,bg="#57a1f8").place(x=0,y=0)

    Label(enc,text="SECRECY",bg="#57a1f8",fg="white",font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=51,y=5)

    #first frame
    f=Frame(enc,bd=3,bg="black",width=450,height=420,relief=GROOVE)
    f.place(x=10,y=48)

    lbl=Label(f,bg="black")
    lbl.place(x=40,y=10)

    #second frame
    Label(enc,text="Enter your message (Special Characters not Allowed)",bg="#57a1f8",fg="white",font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=465,y=25)
    frame2=Frame(enc,bd=3,width=450,height=320,bg="white",relief=GROOVE)
    frame2.place(x=465,y=50)

    text1=Text(frame2,font="Robote 14",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=320)
    
    scrollbar1=Scrollbar(frame2)
    scrollbar1.place(x=428,y=0,height=310)

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)

    #fifth frame
    Label(enc,text="Enter 5 Character Watermark",bg="#57a1f8",fg="white",font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=465,y=380)
    frame5=Frame(enc,bd=3,width=450,height=54,bg="white",relief=GROOVE)
    frame5.place(x=465,y=410)

    text2=Text(frame5,font="Robote 14",bg="white",fg="black",relief=GROOVE)
    text2.place(x=0,y=0,width=430,height=54)

    scrollbar2=Scrollbar(frame5)
    scrollbar2.place(x=428,y=0,height=55)

    scrollbar2.configure(command=text2.yview)
    text2.configure(yscrollcommand=scrollbar2.set)


    #third frame
    frame3=Frame(enc,bd=3,bg="#57a1f8",width=450,height=100,relief=GROOVE)
    frame3.place(x=10,y=470)

    Button(frame3,text="Open Image",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=showimage).place(x=28,y=20)
    Button(frame3,text="Save Image",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=save).place(x=284,y=20)
    #Label(frame3,text="Picture, Image, Photo File",bg="#57a1f8",fg="yellow").place(x=20,y=5)

    #fourth frame
    frame4=Frame(enc,bd=3,bg="#57a1f8",width=450,height=100,relief=GROOVE)
    frame4.place(x=465,y=470)

    Button(frame4,text="Encode",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=Hide).place(x=28,y=20)
    Button(frame4,text="Exit",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=esc).place(x=282,y=20)
    #Label(frame4,text="Picture, Image, Photo File",bg="#57a1f8",fg="yellow").place(x=20,y=5)

#decode Window starts-------------------------------------------
flag=0
def decode():
    global logo
    mid.destroy()
    dec=Tk()
    dec.title("Secrecy - Hide secret text message in image")
    dec.geometry('925x600+300+200')
    dec.configure(bg="#57a1f8")
    dec.resizable(False, False)

    def showimage():
        global flag
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPEG File","*.jpeg"),
                                                   ("All File","*.txt")))
        img=Image.open(filename)
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img,width=250,height=250)
        lbl.image=img
        flag=1

    def esc():
        answer = messagebox.askquestion("Exit Application", "Do you really want to exit?")
        if answer=='yes':
           dec.destroy()

    def Show():
        if flag ==0:
            messagebox.showerror("Invalid","Image not selected")
            decode()

        w=text2.get("1.0","end-1c")
        
        if len(w)!=5:
            messagebox.showerror("Invalid","Invalid watermark!")
            text2.delete("1.0","end-1c")
            text1.delete("1.0","end-1c")
            decode()
            
        clear_message=LSB.reveal(filename)
        str2=clear_message
        
            
        if len(str2)>=9999:
            messagebox.showerror("Error","Image doesnt contain any message")
            text2.delete("1.0","end-1c")
            text1.delete("1.0","end-1c")
            decode()
    
        str3,watermark=LSB.decrypt(str2)
        
        if len(w) == 5:
            watermark1= w
            if watermark1 == watermark:
                text1.delete("1.0","end-1c")
                messagebox.showinfo("Success","Message Decoded Successfully")
                text1.insert("end-1c",str3)
            else:
                messagebox.showerror("Invalid","Watermark did not match")
                text2.delete("1.0","end-1c")
                text1.delete("1.0","end-1c")
                decode()
        else:
            messagebox.showerror("Invalid","Invalid watermark!")
            text2.delete("1.0","end-1c")
            text1.delete("1.0","end-1c")
            decode()
        

    #icon
    image_icon=PhotoImage(file="asset/logon.png")
    dec.iconphoto(False,image_icon)

    #logo
    logo=PhotoImage(file="asset/logo.png")
    Label(dec,image=logo,bg="#57a1f8").place(x=0,y=0)

    Label(dec,text="SECRECY",bg="#57a1f8",fg="white",font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=51,y=5)

    #first frame
    f=Frame(dec,bd=3,bg="black",width=450,height=420,relief=GROOVE)
    f.place(x=10,y=48)

    lbl=Label(f,bg="black")
    lbl.place(x=40,y=10)

    #second frame
    Label(dec,text="Decoded Message",bg="#57a1f8",fg="white",font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=465,y=25)
    frame2=Frame(dec,bd=3,width=450,height=320,bg="white",relief=GROOVE)
    frame2.place(x=465,y=50)

    text1=Text(frame2,font="Robote 14",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=320)

    scrollbar1=Scrollbar(frame2)
    scrollbar1.place(x=428,y=0,height=310)

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)

    #fifth frame
    Label(dec,text="Enter 5 Character Watermark",bg="#57a1f8",fg="white",font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=465,y=380)
    frame5=Frame(dec,bd=3,width=450,height=54,bg="white",relief=GROOVE)
    frame5.place(x=465,y=410)

    text2=Text(frame5,font="Robote 14",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text2.place(x=0,y=0,width=430,height=54)

    scrollbar2=Scrollbar(frame5)
    scrollbar2.place(x=428,y=0,height=55)

    scrollbar2.configure(command=text2.yview)
    text2.configure(yscrollcommand=scrollbar2.set)

    #third frame
    frame3=Frame(dec,bd=3,bg="#57a1f8",width=910,height=100,relief=GROOVE)
    frame3.place(x=10,y=470)

    Button(frame3,text="Open Image",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=showimage).place(x=40,y=20)
    #Label(frame3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

    #fourth frame
    #frame4=Frame(dec,bd=3,bg="#57a1f8",width=450,height=100,relief=GROOVE)
    #frame4.place(x=465,y=470)

    Button(frame3,text="Decode",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=Show).place(x=400,y=20)
    Button(frame3,text="Exit",width=10,height=2,font=('Microsoft YaHei UI Light', 11, 'bold'),command=esc).place(x=750,y=20)
    #Label(frame4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)


#Login Window Starts-------------------------------------------
def main_screen():
    global root
    global user
    global code
    global img
    root=Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False, False)

    image_icon=PhotoImage(file="asset/logo.jpg")
    root.iconphoto(False,image_icon)

    img=PhotoImage(file="asset/logon.png")
    Label(root,image=img, bg='white').place(x=50,y=50)

    frame=Frame(root, width=350,height=350, bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100,y=5)

    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
        
    user=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2, bg='black').place(x=25,y=107)
    
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    
    code=Entry(frame, width=25, fg='black',show='*', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    
    code.insert(0,"Password")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    
    Frame (frame, width=295,height=2, bg='black').place(x=25,y=177)

    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=270)

    sign_up= Button (frame,width=6, text='Sign up', border=0, bg='white', cursor = 'hand2', fg='#57a1f8',command=signup_command)
    sign_up.place(x=215,y=270)
    root.mainloop()

main_screen()
