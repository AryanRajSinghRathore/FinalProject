import tkinter as tkr
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser as wb

app =tkr.Tk(__name__)
app.title('ARYAN GROCERY STORE')
app.geometry('1000x900')
app.iconbitmap('logo.ico')

img =Image.open('index.jpg')
img_resized= img.resize((900,750))
img2 =ImageTk.PhotoImage(img_resized)
tkr.Label(app, image=img2).pack()

tkr.Label(app,text='WELCOME TO GROCERY STORE', font=('Arial', 20)).place(x=350, y=50)
tkr.Label(app,text='ENTER YOUR EMAIL', font=('Arial', 10)).place(x=455, y=270)
tkr.Label(app,text='ENTER YOUR PASSWORD', font=('Arial', 10)).place(x=455, y=330)
tkr.Label(app,text='OR', font=('Arial', 10)).place(x=490, y=440)

fv= tkr.Variable(app)
sv= tkr.Variable(app)


#ENTRY
tkr.Entry(app, width=25,textvariable=fv, font=('Arial',12)).place(x=455,y=300)
tkr.Entry(app, width=25,textvariable=sv, font=('Arial',12)).place(x=455,y=360)

def cred():
        email = 'aryan123@gmail.com'
        password = '12345678'
        a=sv.get()
        b=fv.get()
        if email == b and password == a:
            #messagebox.showinfo('congrats','SUCCESSFULLY LOGGED IN')
            app.destroy()
            home()
        
        else:
              messagebox.showerror('invalid','oops something went wrong')


def guest():
    app.destroy()
    b =tkr.Tk(__name__)
    b.title('GROCERY STORE')
    b.geometry('1000x900')
    b.iconbitmap('logo.ico')
    b.destroy()
    home()
        
def acc():
    c = tkr.Tk(__name__)
    c.title('ACCOUNTS')
    c.geometry('400x300')
    c.iconbitmap('logo.ico')

        
    def ok():
        c.destroy()
        
        

    tkr.Label(c,text='ACCOUNT', font=('Arial', 20),bg='blue',fg='black').place(x=90, y=0)

    tkr.Label(c,text='NAME:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=50)
    tkr.Label(c,text='ARYAN RAJ SING RATHORE', font=('Arial', 10),fg='black').place(x=100, y=50)
    tkr.Label(c,text='ADSRESS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=80)
    tkr.Label(c,text='XYZ PLOT,STREET', font=('Arial', 10),fg='black').place(x=100, y=80)
    tkr.Label(c,text='PINCODE:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=110)
    tkr.Label(c,text='302021', font=('Arial', 10),fg='black').place(x=100, y=110)

    tkr.Button(c,text='OK',command=ok,width=5,font=(10)).place(x=150,y=190)



def home():
        a = tkr.Tk(__name__)
        a.title('GROCERY STORE')
        a.geometry('1000x900')
        a.iconbitmap('logo.ico')
        
        img =Image.open('market.png')
        img_resized= img.resize((150,50))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=150, height=30)
        label.image=img2
        label.place(x=0,y=0)

        img =Image.open('sp3.jpg')
        img_resized= img.resize((300,120))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=300, height=120)
        label.image=img2
        label.place(x=690,y=0)

        img =Image.open('line.png')
        img_resized= img.resize((3,770))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=3, height=770)
        label.image=img2
        label.place(x=220,y=50)

        img =Image.open('w2.jpeg')
        img_resized= img.resize((300,230))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=300, height=230)
        label.image=img2
        label.place(x=240,y=100)

        img =Image.open('w3.jpeg')
        img_resized= img.resize((300,230))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=300, height=230)
        label.image=img2
        label.place(x=580,y=100)

        img =Image.open('w4.jpeg')
        img_resized= img.resize((300,230))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=300, height=230)
        label.image=img2
        label.place(x=240,y=390)

        img =Image.open('w5.jpeg')
        img_resized= img.resize((300,230))
        img2 =ImageTk.PhotoImage(img_resized)
        label = tkr.Label(a, image=img2, width=300, height=230)
        label.image=img2
        label.place(x=580,y=390)


        def vege():
                a.destroy()
                oil()

        def snc():
                a.destroy()
                snacks()
                
        def dy():
                a.destroy()
                daily1()

        def mr():
                a.destroy()
                more()
        z=tkr.Variable(a)

        def choice():
                choice=z.get()
                if choice == 'oil':
                        a.destroy()
                        oil()

                elif choice =='chips':
                        a.destroy()
                        snacks()
               

                elif choice == 'flour':
                        a.destroy()
                        daily1()

                else:
                        a.destroy()
                        more()

        def ama():
                wb.open('https://www.amazon.in/alm/storefront?almBrandId=ctnow')

        
        def flip():
                wb.open('https://www.flipkart.com/grocery-supermart-store?marketplace=GROCERY')

        def big():
                wb.open('https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-JPR&gclid=CjwKCAiA7IGcBhA8EiwAFfUDsaD3R3cbizEJVAiD1LGDEnKI3Q2x8qQLSTq1XnFSU1X52vfXgZwRjRoCyvMQAvD_BwE')

        def blink():
                wb.open('https://blinkit.com/?%243p=a_google_adwords&%24always_deeplink=false&gclid=CjwKCAiA7IGcBhA8EiwAFfUDsTzsVFMit50EeHXtalb4FO2kQwJPndeMDNuT5DWiYxboSQsYTIT38BoCPvsQAvD_BwE&gclid=CjwKCAiA7IGcBhA8EiwAFfUDsTzsVFMit50EeHXtalb4FO2kQwJPndeMDNuT5DWiYxboSQsYTIT38BoCPvsQAvD_BwE&lpurl=https%3A%2F%2Fblinkit.com%2F%3Fgclsrc%3Daw.ds%26&~ad_set_id=125400797949&~campaign_id=14296948532&~channel=g&~keyword=blinkit&~placement&_branch_match_id=1124920106824457981&_branch_referrer=H4sIAAAAAAAAA7WPXU%2BDMBSGfw1cApYywIQYxoebOt0iTndFCi1Q6aCh3br566WLf8Hk3Jz3ycl53k5KLu5tu52aSViIc4vRobelz1O4L1YvtHowAHR5hMp2HFtGSoTVOGFhzjFiCl1FiQnh%2BipqEBPEbGtGcZR8q%2BckprG%2FfqyXXRxkVMV585GK4kfs8w2VnpOR1ZdErIL5G%2Bh36mk7YLJJX0%2BFl37Sw6Ua33fiUKwLN1iOyfYsdvE5LZcqMxk%2FTSzqtLrhxgbI56m0AZVWPR514Oazhphqw02RsrAwwMI0%2FAzhUhBZzn53wIOO44d%2BCENNanTkiLbDjUEQLkIYeC64oQ4NA2FRq5eeXHX%2F6O%2Ff%2F7f9BYgU0gqiAQAA')

        #button
        tkr.Button(a, text='ACCOUNTS', command=acc ,width=10,bg='blue', fg='black', font=(10)).place(x=130,y=0)

                
        tkr.Label(a,text='GROCERY STORE', font=('Arial', 20)).place(x=285, y=0)
                        
        tkr.Entry(a,width=40,textvariable=z,font=('Arial',12)).place(x=240,y=40)

        tkr.Button(a, text='search',command=choice,width=10, fg='black', font=(10)).place(x=610,y=35)

        tkr.Label(a,text='MENU',bg='yellow', font=('Brush Script MT', 20)).place(x=25, y=45)
                
        tkr.Button(a, text='<VEGETABLE OILS>',command=vege,width=20,bg='red', fg='black', font=(10)).place(x=10,y=95)
        tkr.Button(a, text='<SNACKS>',command=snc,width=20,bg='red', fg='black', font=(10)).place(x=10,y=145)
        tkr.Button(a, text='<DAILY NEEDS>',command=dy,width=20,bg='red', fg='black', font=(10)).place(x=10,y=195)
        tkr.Button(a, text='<MORE ITEMS>',command=mr,width=20,bg='red', fg='black', font=(10)).place(x=10,y=245)

        tkr.Label(a,text='ABOUT US:', font=('Arial', 10)).place(x=15, y=545)
        tkr.Label(a,text='ARYAN GS--XYZ Industries', font=('Arial', 10)).place(x=15, y=565)
        tkr.Label(a,text='CONTACT US:', font=('Arial', 10)).place(x=15, y=585)
        tkr.Label(a,text='Ph-123445690', font=('Arial', 10)).place(x=15, y=605)
        tkr.Label(a,text='Email--xyz@industries.com', font=('Arial', 10)).place(x=15, y=625)
         
        tkr.Label(a,text='COMPARE US WITH:', font=('Arial', 10)).place(x=15, y=345)
        tkr.Button(a, text='<AMAZON>',command=ama,width=10,bg='blue', fg='black', font=(10)).place(x=10,y=365)
        tkr.Button(a, text='<FLIPKART>',command=flip,width=10,bg='blue', fg='black', font=(10)).place(x=10,y=395)
        tkr.Button(a, text='<BIG BASKET>',command=big,width=10,bg='blue', fg='black', font=(10)).place(x=10,y=425)
        tkr.Button(a, text='<BLINK IT>',command=blink,width=10,bg='blue', fg='black', font=(10)).place(x=10,y=455)
        
        tkr.Button(a, text='Shop Now',command=dy,width=10,bg='white', fg='black', font=(10)).place(x=270,y=275)
        tkr.Button(a, text='Shop Now',command=snc,width=10,bg='white', fg='black', font=(10)).place(x=600,y=275)
        tkr.Button(a, text='Shop Now',command=vege,width=10,bg='white', fg='black', font=(10)).place(x=270,y=555)
        tkr.Button(a, text='Shop Now',command=mr,width=10,bg='white', fg='black', font=(10)).place(x=600,y=560)


        





def oil():
    d =tkr.Tk(__name__)
    d.title('GROCERY STORE')
    d.geometry('1000x900')
    d.iconbitmap('logo.ico')
    img =Image.open('market.png')
    img_resized= img.resize((150,50))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=150, height=30)
    label2.image=img2
    label2.place(x=0,y=0)
    tkr.Label(d,text='Vegetable Oil',font=('Arial',30),fg='black').place(x=365,y=0)

    

    img =Image.open('s1.webp')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=80)

   


    img =Image.open('o2.webp')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=80)

    
    img =Image.open('c1.jpg')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=80)
   

    
    img =Image.open('c2.webp')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=310)
    

    
    img =Image.open('o1.jpg')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=310)
    o1=tkr.Variable(d)
    tkr.Label(d,text='COMBO PACK ->Rs10180', font=('Arial', 10)).place(x=365, y=440)
    tkr.Entry(d,width=3,textvariable=o1,font=('Arial',12)).place(x=420,y=460)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=460)


    
    img =Image.open('c3.webp')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=310)
    c3=tkr.Variable(d)
    tkr.Label(d,text='Chambal oil ->Rs380', font=('Arial', 10)).place(x=700, y=440)
    tkr.Entry(d,width=3,textvariable=c3,font=('Arial',12)).place(x=770,y=460)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=460)


    
    img =Image.open('p1.webp')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=510)
   

    
    img =Image.open('p2.png')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=510)
    

    
    img =Image.open('p4.webp')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(d, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=510)
    p4=tkr.Variable(d)
    tkr.Label(d,text='Parampara refined oil ->Rs180', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(d,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)

    s1=tkr.Variable(d)
    c1=tkr.Variable(d)
    c2=tkr.Variable(d)
    c3=tkr.Variable(d)
    o1=tkr.Variable(d)
    o2=tkr.Variable(d)
    p1=tkr.Variable(d)
    p2=tkr.Variable(d)
    p4=tkr.Variable(d)

    def kart():
        k = tkr.Tk(__name__)
        k.title('ACCOUNTS')
        k.geometry('400x300')
        k.iconbitmap('logo.ico')

        a=s1.get()
        b=c1.get()
        c=c2.get()
        d=c3.get()
        e=o1.get()
        f=o2.get()
        g=p1.get()
        h=p2.get()
        i=p4.get()

        total= eval(a+'+'+b+'+'+c+'+'+d+'+'+e+'+'+f+'+'+g+'+'+h+'+'+i)
        item=total*180   
        def ok():
                k.destroy()
                messagebox.showinfo('CONGO','YOUR ORDER DONE SUCCESFULLY')


        tkr.Label(k,text='ITEM KART', font=('Arial', 20),bg='red',fg='black').place(x=90, y=0)

        tkr.Label(k,text='TOTAL ITEMS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=50)
        tkr.Label(k,text=total, font=('Arial', 10),fg='black').place(x=130, y=50)
        tkr.Label(k,text='TOTAL RS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=80)
        tkr.Label(k,text=item, font=('Arial', 10),fg='black').place(x=100, y=80)
        tkr.Label(k,text='DELIVER TO:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=110)
        tkr.Label(k,text='MR.ARYAN RAJ SINGH RATHORE', font=('Arial', 10),fg='black').place(x=100, y=110)

        tkr.Button(k,text='order',command=ok,width=10,font=(10)).place(x=150,y=190)

    def b1():
            d.destroy()
            home()
    
            


    tkr.Label(d,text='musturd oil ->Rs180', font=('Arial', 10)).place(x=25, y=220)
    tkr.Entry(d,width=3,textvariable=s1,font=('Arial',12)).place(x=80,y=240)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=240)

    tkr.Label(d,text='olive oil -> Rs2000', font=('Arial', 10)).place(x=365, y=220)
    tkr.Entry(d,width=3,textvariable=o2,font=('Arial',12)).place(x=420,y=240)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=240)

    tkr.Label(d,text='Chambal refined oil ->Rs160', font=('Arial', 10)).place(x=705, y=220)
    tkr.Entry(d,width=3,textvariable=c1,font=('Arial',12)).place(x=770,y=240)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=240)
    
    tkr.Label(d,text='bottle packed oil ->Rs280', font=('Arial', 10)).place(x=25, y=440)
    tkr.Entry(d,width=3,textvariable=c2,font=('Arial',12)).place(x=80,y=460)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=460)

    tkr.Label(d,text='Parampara refined oil ->Rs2180', font=('Arial', 10)).place(x=25, y=640)
    tkr.Entry(d,width=3,textvariable=p1,font=('Arial',12)).place(x=80,y=660)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=660)


    tkr.Label(d,text='Parampara refined oil ->Rs180', font=('Arial', 10)).place(x=365, y=640)
    tkr.Entry(d,width=3,textvariable=p2,font=('Arial',12)).place(x=420,y=660)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=660)

    tkr.Label(d,text='Parampara refined oil ->Rs180', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(d,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(d,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)


    tkr.Button(d, text='KART', width=10,command=kart, bg='red' , fg='black', font=(10)).place(x=690,y=10)
    tkr.Button(d,text='HOME',width=10,command=b1,bg='yellow',font=(10)).place(x=790,y=10)



def snacks():
    e =tkr.Tk(__name__)
    e.title('GROCERY STORE')
    e.geometry('1000x900')
    e.iconbitmap('logo.ico')
    img =Image.open('market.png')
    img_resized= img.resize((150,50))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=150, height=30)
    label2.image=img2
    label2.place(x=0,y=0)
    tkr.Label(e,text='SNACKS',font=('Arial',30),fg='black').place(x=365,y=0)

    

    img =Image.open('bingo.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=80)

   


    img =Image.open('ch.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=80)

    
    img =Image.open('cold.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=80)
   

    
    img =Image.open('mc.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=310)
    

    
    img =Image.open('moong.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=310)
    o1=tkr.Variable(e)
    tkr.Label(e,text='MOONG DAL->Rs100', font=('Arial', 10)).place(x=365, y=440)
    tkr.Entry(e,width=3,textvariable=o1,font=('Arial',12)).place(x=420,y=460)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=460)


    
    img =Image.open('roasty.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=310)
    c3=tkr.Variable(e)
    tkr.Label(e,text='ROASTY TASTY ->Rs100', font=('Arial', 10)).place(x=700, y=440)
    tkr.Entry(e,width=3,textvariable=c3,font=('Arial',12)).place(x=770,y=460)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=460)


    
    img =Image.open('soya.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=510)
   

    
    img =Image.open('too.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=510)
    

    
    img =Image.open('bis.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(e, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=510)
    p4=tkr.Variable(e)
    tkr.Label(e,text='ALL BISCUITS ->Rs180', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(e,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)

    s1=tkr.Variable(e)
    c1=tkr.Variable(e)
    c2=tkr.Variable(e)
    c3=tkr.Variable(e)
    o1=tkr.Variable(e)
    o2=tkr.Variable(e)
    p1=tkr.Variable(e)
    p2=tkr.Variable(e)
    p4=tkr.Variable(e)

    def kart():
        k = tkr.Tk(__name__)
        k.title('KART')
        k.geometry('400x300')
        k.iconbitmap('logo.ico')

        a=s1.get()
        b=c1.get()
        c=c2.get()
        d=c3.get()
        e=o1.get()
        f=o2.get()
        g=p1.get()
        h=p2.get()
        i=p4.get()

        total= eval(a+'+'+b+'+'+c+'+'+d+'+'+e+'+'+f+'+'+g+'+'+h+'+'+i)
        item=total*100   
        def ok():
                k.destroy()
                messagebox.showinfo('CONGO','YOUR ORDER DONE SUCCESFULLY')


        tkr.Label(k,text='ITEM KART', font=('Arial', 20),bg='red',fg='black').place(x=90, y=0)

        tkr.Label(k,text='TOTAL ITEMS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=50)
        tkr.Label(k,text=total, font=('Arial', 10),fg='black').place(x=130, y=50)
        tkr.Label(k,text='TOTAL RS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=80)
        tkr.Label(k,text=item, font=('Arial', 10),fg='black').place(x=100, y=80)
        tkr.Label(k,text='DELIVER TO:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=110)
        tkr.Label(k,text='MR.ARYAN RAJ SINGH RATHORE', font=('Arial', 10),fg='black').place(x=100, y=110)

        tkr.Button(k,text='ORDER',command=ok,width=10,font=(10)).place(x=150,y=190)

    def b2():
            e.destroy()
            home()

        
    tkr.Label(e,text='BINGO ->Rs18', font=('Arial', 10)).place(x=25, y=220)
    tkr.Entry(e,width=3,textvariable=s1,font=('Arial',12)).place(x=80,y=240)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=240)

    tkr.Label(e,text='CADBUARY SILK-> Rs200', font=('Arial', 10)).place(x=365, y=220)
    tkr.Entry(e,width=3,textvariable=o2,font=('Arial',12)).place(x=420,y=240)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=240)

    tkr.Label(e,text='ALL COLD DRINKS ->Rs160', font=('Arial', 10)).place(x=705, y=220)
    tkr.Entry(e,width=3,textvariable=c1,font=('Arial',12)).place(x=770,y=240)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=240)
    
    tkr.Label(e,text='McCAIN ->Rs280', font=('Arial', 10)).place(x=25, y=440)
    tkr.Entry(e,width=3,textvariable=c2,font=('Arial',12)).place(x=80,y=460)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=460)

    tkr.Label(e,text='TOO YUM ->Rs21', font=('Arial', 10)).place(x=25, y=640)
    tkr.Entry(e,width=3,textvariable=p1,font=('Arial',12)).place(x=80,y=660)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=660)


    tkr.Label(e,text='ALL BISCUITS ->Rs180', font=('Arial', 10)).place(x=365, y=640)
    tkr.Entry(e,width=3,textvariable=p2,font=('Arial',12)).place(x=420,y=660)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=660)

    tkr.Label(e,text='SOYA STICKS PACK ->Rs180', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(e,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(e,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)


    tkr.Button(e, text='KART', width=10,command=kart, bg='red' , fg='black', font=(10)).place(x=690,y=10)
    tkr.Button(e,text='HOME',width=10,command=b2,bg='yellow',font=(10)).place(x=790,y=10)



def daily1():
    f =tkr.Tk(__name__)
    f.title('GROCERY STORE')
    f.geometry('1000x900')
    f.iconbitmap('logo.ico')
    img =Image.open('market.png')
    img_resized= img.resize((150,50))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=150, height=30)
    label2.image=img2
    label2.place(x=0,y=0)
    tkr.Label(f,text='DAILY PRODUCTS',font=('Arial',30),fg='black').place(x=325,y=0)

    

    img =Image.open('d1.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=80)

    img =Image.open('d2.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=80)

    
    img =Image.open('d3.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=80)
   

    
    img =Image.open('d4.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=310)
    

    
    img =Image.open('d5.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=310)
    o1=tkr.Variable(f)
    tkr.Label(f,text='TURMERIC POWDER->Rs170', font=('Arial', 10)).place(x=365, y=440)
    tkr.Entry(f,width=3,textvariable=o1,font=('Arial',12)).place(x=420,y=460)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=460)
    
    img =Image.open('d6.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=310)
    c3=tkr.Variable(f)
    tkr.Label(f,text='MIRCHI POWDER ->Rs160', font=('Arial', 10)).place(x=700, y=440)
    tkr.Entry(f,width=3,textvariable=c3,font=('Arial',12)).place(x=770,y=460)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=460)
  
    img =Image.open('d7.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=510)
    
    img =Image.open('d8.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=510)
      
    img =Image.open('d9.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(f, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=510)
    p4=tkr.Variable(f)
    tkr.Label(f,text='ALL BISCUITS ->Rs180', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(f,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)

    s1=tkr.Variable(f)
    c1=tkr.Variable(f)
    c2=tkr.Variable(f)
    c3=tkr.Variable(f)
    o1=tkr.Variable(f)
    o2=tkr.Variable(f)
    p1=tkr.Variable(f)
    p2=tkr.Variable(f)
    p4=tkr.Variable(f)

    def kart():
        k = tkr.Tk(__name__)
        k.title('KART')
        k.geometry('400x300')
        k.iconbitmap('logo.ico')

        a=s1.get()
        b=c1.get()
        c=c2.get()
        d=c3.get()
        e=o1.get()
        f=o2.get()
        g=p1.get()
        h=p2.get()
        i=p4.get()

        total= eval(a+'+'+b+'+'+c+'+'+d+'+'+e+'+'+f+'+'+g+'+'+h+'+'+i)
        item=total*179   
        def ok():
                k.destroy()
                messagebox.showinfo('CONGO','YOUR ORDER DONE SUCCESFULLY')


        tkr.Label(k,text='ITEM KART', font=('Arial', 20),bg='red',fg='black').place(x=90, y=0)

        tkr.Label(k,text='TOTAL ITEMS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=50)
        tkr.Label(k,text=total, font=('Arial', 10),fg='black').place(x=130, y=50)
        tkr.Label(k,text='TOTAL RS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=80)
        tkr.Label(k,text=item, font=('Arial', 10),fg='black').place(x=100, y=80)
        tkr.Label(k,text='DELIVER TO:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=110)
        tkr.Label(k,text='MR.ARYAN RAJ SINGH RATHORE', font=('Arial', 10),fg='black').place(x=100, y=110)

        tkr.Button(k,text='ORDER',command=ok,width=10,font=(10)).place(x=150,y=190)

    def b2():
            f.destroy()
            home()

        
    tkr.Label(f,text='FLOUR ->Rs18', font=('Arial', 10)).place(x=25, y=220)
    tkr.Entry(f,width=3,textvariable=s1,font=('Arial',12)).place(x=80,y=240)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=240)

    tkr.Label(f,text='BRIYANI SPECIAL RICE-> Rs200', font=('Arial', 10)).place(x=365, y=220)
    tkr.Entry(f,width=3,textvariable=o2,font=('Arial',12)).place(x=420,y=240)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=240)

    tkr.Label(f,text='SUGAR ->Rs160', font=('Arial', 10)).place(x=705, y=220)
    tkr.Entry(f,width=3,textvariable=c1,font=('Arial',12)).place(x=770,y=240)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=240)
    
    tkr.Label(f,text='TEA->Rs280', font=('Arial', 10)).place(x=25, y=440)
    tkr.Entry(f,width=3,textvariable=c2,font=('Arial',12)).place(x=80,y=460)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=460)
    
    tkr.Label(f,text='CORRANDER POWDER ->Rs210', font=('Arial', 10)).place(x=25, y=640)
    tkr.Entry(f,width=3,textvariable=p1,font=('Arial',12)).place(x=80,y=660)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=660)


    tkr.Label(f,text='SAUCES VALUE PACK ->Rs180', font=('Arial', 10)).place(x=365, y=640)
    tkr.Entry(f,width=3,textvariable=p2,font=('Arial',12)).place(x=420,y=660)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=660)

    tkr.Label(f,text='TATA SALT ->Rs18', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(f,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(f,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)


    tkr.Button(f, text='KART', width=10,command=kart, bg='red' , fg='black', font=(10)).place(x=690,y=10)
    tkr.Button(f,text='HOME',width=10,command=b2,bg='yellow',font=(10)).place(x=790,y=10)




def more():
    g=tkr.Tk(__name__)
    g.title('GROCERY STORE')
    g.geometry('1000x900')
    g.iconbitmap('logo.ico')
    img =Image.open('market.png')
    img_resized= img.resize((150,50))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=150, height=30)
    label2.image=img2
    label2.place(x=0,y=0)
    tkr.Label(g,text='MORE ITEMS',font=('Arial',30),fg='black').place(x=325,y=0)

    

    img =Image.open('m1.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=80)

    img =Image.open('m2.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=80)

    
    img =Image.open('m3.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=80)
   

    
    img =Image.open('m4.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=310)
    

    
    img =Image.open('m5.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=310)
    o1=tkr.Variable(g)
    tkr.Label(g,text='BEVERAGES->Rs170', font=('Arial', 10)).place(x=365, y=440)
    tkr.Entry(g,width=3,textvariable=o1,font=('Arial',12)).place(x=420,y=460)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=460)


    
    img =Image.open('m6.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=310)
    c3=tkr.Variable(g)
    tkr.Label(g,text='MAGGIE ->Rs84', font=('Arial', 10)).place(x=700, y=440)
    tkr.Entry(g,width=3,textvariable=c3,font=('Arial',12)).place(x=770,y=460)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=460)


    
    img =Image.open('m7.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=690,y=510)
   

    
    img =Image.open('m8.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=10,y=510)
    

    
    img =Image.open('m9.jfif')
    img_resized= img.resize((200,130))
    img2 =ImageTk.PhotoImage(img_resized)
    label2 = tkr.Label(g, image=img2, width=200, height=130)
    label2.image=img2
    label2.place(x=350,y=510)

    s1=tkr.Variable(g)
    c1=tkr.Variable(g)
    c2=tkr.Variable(g)
    c3=tkr.Variable(g)
    o1=tkr.Variable(g)
    o2=tkr.Variable(g)
    p1=tkr.Variable(g)
    p2=tkr.Variable(g)
    p4=tkr.Variable(g)

    def kart():
        k = tkr.Tk(__name__)
        k.title('KART')
        k.geometry('400x300')
        k.iconbitmap('logo.ico')

        a=s1.get()
        b=c1.get()
        c=c2.get()
        d=c3.get()
        e=o1.get()
        f=o2.get()
        g=p1.get()
        h=p2.get()
        i=p4.get()

        total= eval(a+'+'+b+'+'+c+'+'+d+'+'+e+'+'+f+'+'+g+'+'+h+'+'+i)
        item=total*149   
        def ok():
                k.destroy()
                messagebox.showinfo('CONGO','YOUR ORDER DONE SUCCESFULLY')


        tkr.Label(k,text='ITEM KART', font=('Arial', 20),bg='red',fg='black').place(x=90, y=0)

        tkr.Label(k,text='TOTAL ITEMS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=50)
        tkr.Label(k,text=total, font=('Arial', 10),fg='black').place(x=130, y=50)
        tkr.Label(k,text='TOTAL RS:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=80)
        tkr.Label(k,text=item, font=('Arial', 10),fg='black').place(x=100, y=80)
        tkr.Label(k,text='DELIVER TO:', font=('Arial', 10),bg='red',fg='black').place(x=30, y=110)
        tkr.Label(k,text='MR.ARYAN RAJ SINGH RATHORE', font=('Arial', 10),fg='black').place(x=100, y=110)

        tkr.Button(k,text='ORDER',command=ok,width=10,font=(10)).place(x=150,y=190)

    def b2():
            g.destroy()
            home()

        
    tkr.Label(g,text='BREAD ->Rs18', font=('Arial', 10)).place(x=25, y=220)
    tkr.Entry(g,width=3,textvariable=s1,font=('Arial',12)).place(x=80,y=240)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=240)

    tkr.Label(g,text='EGGS-> Rs400', font=('Arial', 10)).place(x=365, y=220)
    tkr.Entry(g,width=3,textvariable=o2,font=('Arial',12)).place(x=420,y=240)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=240)

    tkr.Label(g,text='AMUL BUTTER ->Rs120', font=('Arial', 10)).place(x=705, y=220)
    tkr.Entry(g,width=3,textvariable=c1,font=('Arial',12)).place(x=770,y=240)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=240)
    
    tkr.Label(g,text='CHOCOLATE->Rs280', font=('Arial', 10)).place(x=25, y=440)
    tkr.Entry(g,width=3,textvariable=c2,font=('Arial',12)).place(x=80,y=460)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=460)

    tkr.Label(g,text='FRSH MILK ->Rs40', font=('Arial', 10)).place(x=25, y=640)
    tkr.Entry(g,width=3,textvariable=p1,font=('Arial',12)).place(x=80,y=660)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=65,y=660)

    tkr.Label(g,text='BHUJIA VALUE PACK ->Rs140', font=('Arial', 10)).place(x=365, y=640)
    tkr.Entry(g,width=3,textvariable=p2,font=('Arial',12)).place(x=420,y=660)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=405,y=660)

    tkr.Label(g,text='BICUITS ->Rs18', font=('Arial', 10)).place(x=705, y=640)
    tkr.Entry(g,width=3,textvariable=p4,font=('Arial',12)).place(x=770,y=660)
    tkr.Label(g,text='Q',font=('Arial',10),bg='red',fg='black').place(x=755,y=660)

    tkr.Button(g, text='KART', width=10,command=kart, bg='red' , fg='black', font=(10)).place(x=690,y=10)
    tkr.Button(g,text='HOME',width=10,command=b2,bg='yellow',font=(10)).place(x=790,y=10)

#1st page BUTTON
tkr.Button(app, text='SUBMIT', width=10,command=cred, bg='blue' , fg='black', font=(10)).place(x=470,y=400)
tkr.Button(app, text='login as a guest', width=20,command=guest, bg='red' , fg='black', font=(10)).place(x=460,y=470)

app.mainloop() 

