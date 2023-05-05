import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import datetime
import pymysql


my_con=pymysql.connect(
    host='localhost',
    user='root',
    password='vasanth',
    database='python_db_03032023'
)
my_db=my_con.cursor()
print("connected successfully")


win = tk.Tk()
win.geometry("1300x600")
win.title("Mail_Domain")

frame1 = Frame(win)
frame1.pack(ipadx=50,ipady=50,expand=True,fill='both')

bg=ImageTk.PhotoImage(file='bg05.jpg')

canvas=Canvas(frame1)
canvas.pack(fill=BOTH, expand=True)

canvas.create_image(0,0,image=bg,anchor='nw')


def resize_image(e):
   # global image, resized, image2
   # open image to resize it
   image = Image.open("bg05.jpg")
   # resize the image with width and height of window
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

#    Labels
   canvas.create_text(481, 80, text="D", font=('Helvetica 38 bold'), fill='red')
   canvas.pack()
   # canvas.create_text(654, 80, text="U", font=('Helvetica 38 bold'), fill='red')
   # canvas.pack()
   canvas.create_text(780, 80, text="omain-Username Separator", font=('Helvetica 32 bold'), fill='orange')
   canvas.pack()

   canvas.create_text(340,360,text='Mail id',font='Helvetica 20 bold',fill='orange')
   canvas.pack()

   canvas.create_text(1015,280,text='Username',font='Helvetica 20 bold',fill='orange')
   canvas.pack()

   canvas.create_text(1040, 400, text='Domain name', font='Helvetica 20 bold', fill='orange')
   canvas.pack()


   canvas.create_text(790,700, text='Privacy Policy | Disclaimer', font='Helvetica 12', fill='white')
   canvas.pack()

   canvas.create_text(640, 750, text="This Website provides legal information and referrals.\nFor legal advice, contact a lawyer.© 1993-2023 License", font='Helvetica 10', fill='white')
   canvas.pack()

   canvas.create_text(900, 745,text="Connect FB",font='Helvetica 10', fill='white')
   canvas.pack()


   canvas.create_text(940, 760,text="Website by vasanth & Co.",font='Helvetica 10', fill='white')
   canvas.pack()

win.bind("<Configure>",resize_image)


def refresh():
   mail_e.delete(0,END)
   username_txt.delete("1.0","end")
   domain_txt.delete("1.0","end")


def conversion():
    mail=mail_e.get()

    #History

    now = datetime.now()
    t=now.strftime("%H:%M:%S")

    if "@" and ".com" not in mail:
       print("please mention the domain")
       messagebox.showerror('Error','Please enter a correct mail id')
    else:
       print(mail.index('@'))
       at=mail.index('@')
       domain=mail[at+1:]
       username=mail[:at]
       print("domain =",domain)
       print("Username = ",username)
       username_txt.insert(END,username)
       domain_txt.insert(END,domain)

       now = datetime.now()
       t = now.strftime("%H:%M:%S")

       #inserting to db
       query1='insert into mailidsep(mail, name,domain,time) values(%s,%s,%s,%s)'
       values=(mail,username,domain,t)
       my_db.execute(query1,values)
       my_con.commit()

       file = open("C:\\Users\\vasanth rohith\\2023_python\\weekly_projects\\mailidsep_030423\\history.txt", 'a')
       file.write(mail + '    ' + t)
       file.write('\n')

       file.close()


# frame1 labels
# header = Label(frame1,text='Domain-Username Separator',font='Helvetica 24 bold',
#                bg='light blue',highlightcolor="purple",highlightthickness=4)
# header.pack(pady=50)

# mail_l=Label(frame1,text='Mail id',font='Helvetica 20 bold',bg='light blue')
# mail_l.place(x=180,y=300)

# username_l=Label(frame1,text='Username',font='Helvetica 20 bold',bg='light blue')
# username_l.place(x=870,y=250)



# entries
mail_en=StringVar()
mail_e=Entry(frame1,width=40,textvariable=mail_en)
mail_e.place(x=410,y=350)

username_txt=Text(frame1,height=1,width=30)
username_txt.place(x=950,y=300)

domain_txt=Text(frame1,height=1,width=30)
domain_txt.place(x=950,y=420)

# Buttons

convert_btn=Button(frame1,text='Next',width=5,font='Helvetica 12 bold',borderwidth=5,command=conversion)
convert_btn.place(x=740,y=330)

refresh_btn=Button(frame1,text='Refresh',width=7,font='Helvetica 12 bold',borderwidth=5,command=refresh)
refresh_btn.place(x=731,y=380)






win.mainloop()