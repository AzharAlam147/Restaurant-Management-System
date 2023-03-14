from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import time
class Login_system:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("600x534")
        #----------variables------------#
        self.u_name=StringVar()
        self.u_pass=StringVar()
        #------------Image--------------#
        self.bg_icon = ImageTk.PhotoImage(file="rest.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="image.jpg")
        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="-:Welcome To Restaurent Management System:-",
                      font=("Cambria", 20,"bold", "underline"),fg="steelblue",bg="Black")
        title.place(x=0,y=0,relwidth=1)
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=40,y=90)

        logo_lbl = Label(login_frame,image=self.logo_icon).grid(row=0,column=0,padx=0,pady=0)
        lbl_admin = Label(login_frame,text="-:Admin Login:-",compound=RIGHT,font=("cambria",20,"bold"),bg="white").grid(row=0,column=1,padx=0,pady=0)
        lbluser = Label(login_frame,text="UserName:-",compound=LEFT,font=("cambria",14,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txt_user=Entry(login_frame,bd=5,textvariable=self.u_name,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        lbluser = Label(login_frame, text="Password:-", compound=LEFT, font=("cambria", 14, "bold"), bg="white").grid(
            row=3, column=0, padx=20, pady=10)
        txt_pass = Entry(login_frame, bd=5, textvariable=self.u_pass,relief=GROOVE, font=("", 15)).grid(row=3, column=1, padx=20)
        btn_login=Button(login_frame,text="Login",width=15,command=self.login_admin,font=("cambria",15,"bold"),bg="steel blue",fg="white").grid(row=4,column=1,pady=10)

    def login_admin(self):
        if self.u_name.get() == "" or self.u_pass.get() == "":
          messagebox.showerror("Error","Please Enter UserName And Password Both")
        elif self.u_name.get() == "admin" and self.u_pass.get() == "admin123":
            messagebox.showinfo("Successfully Login",f"Welcome {self.u_name.get()}")
            root.destroy()
            self.Select = Tk()
            self.Select.geometry("510x100")
            self.Select.title("PANEL")
            btnRmf2 = Button(self.Select, padx=16, pady=3, bd=6, fg="black", font=('ariel', 14, 'bold'), width=17,
                             height=3,
                             text="ADMIN PANEL", bg="powder blue", command=self.Rmf2)
            btnRmf2.place(y=2, x=2)
            btnRmf3 = Button(self.Select, padx=16, pady=3, bd=6, fg="black", font=('ariel', 14, 'bold'), width=17,
                             height=3,
                             text="ORDER", bg="powder blue", command=self.RMF3)
            btnRmf3.place(y=2, x=256)
        else:
            messagebox.showerror("Error","Invalid UserName or Password")

    def Selection(self):
        root.destroy()
        self.Select = Tk()
        self.Select.geometry("510x100")
        self.Select.title("PANEL")
        btnRmf2 = Button(self.Select, padx=16, pady=3, bd=6, fg="black", font=('ariel', 14, 'bold'), width=17, height=3,
                         text="ADMIN PANEL", bg="powder blue", command=self.Rmf2)
        btnRmf2.place(y=2, x=2)
        btnRmf3 = Button(self.Select, padx=16, pady=3, bd=6, fg="black", font=('ariel', 14, 'bold'), width=17, height=3,
                         text="ORDER", bg="powder blue", command=self.RMF3)
        btnRmf3.place(y=2, x=256)
        self.Select.mainloop()

    def Rmf2(self):
            menu = [("PIZZA", "1000"), ("BRIYANI", "180"), ("TIKKA", "280")]
            # ------------------------------------- ****** SECOND FOAM  ****** -------------------------------------------
            self.Select.withdraw()
            AdminPage = Tk()
            AdminPage.geometry("1000x600")
            AdminPage.title("ADMIN CONTROL")
            Tops = Frame(AdminPage, width=900, height=400, relief=SUNKEN)
            Tops.pack(side=TOP)

            # ------------------TIME--------------
            localtime = time.asctime(time.localtime(time.time()))

            # -----------------INFO TOP------------
            lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", fg="steel blue",
                            bd=10,
                            anchor='w')
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(Tops, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)

            style = ttk.Style()
            style.configure("Treeview", font=('Calibri', 16, 'bold'))  # , rowheight=17
            style.configure("Treeview.Heading", font=('Calibri', 16, 'bold'))  # Modify the font of the headings
            tree = ttk.Treeview(AdminPage)

            tree["columns"] = ("one", "two")
            tree.config(height=17)
            tree.place(y=150, x=480)

            tree.column("#0", width=180, minwidth=200, stretch=NO, anchor="w")
            tree.column("one", width=100, minwidth=100, stretch=NO, anchor="w")

            tree.heading("#0", text=" ITEM ", anchor="center")
            tree.heading("one", text=" PRICE ", anchor="center")

            def Show():

                for ele in sorted(menu):
                    print(ele)
                treeview = tree
                index = iid = 0
                for row in menu:
                    treeview.insert("", index, iid, value=row)
                    index = iid = index + 1

            # ------------------------------------------ TO ADD ITEM ---------------------------------------------
            # --------------------------------- ITEM NAME LABEL AND TEXXTBOX ---------------------------------
            lblAItemName = Label(AdminPage, text="ITEM NAME", font=('ariel', 14, 'bold'))
            lblAItemName.place(y=170, x=20)
            Aitemtxt = StringVar()
            txtAItemName = Entry(AdminPage, font=('ariel', 12, 'bold'), textvariable=Aitemtxt)
            txtAItemName.place(y=173, x=160)

            # --------------------------------- ITEM PRICE LABEL AND TEXXTBOX ---------------------------------
            lblAItemPrice = Label(AdminPage, text="ITEM PRICE", font=('ariel', 14, 'bold'))
            lblAItemPrice.place(y=210, x=20)
            Apricetxt = StringVar()
            txtAItemPrice = Entry(AdminPage, font=('ariel', 12, 'bold'), width=7, textvariable=Apricetxt)
            txtAItemPrice.place(y=213, x=160)
            lblCurrency = Label(AdminPage, text="Rs", font=('ariel', 14, 'bold'))
            lblCurrency.place(y=210, x=240)

            btnAdd = Button(AdminPage, padx=16, pady=3, bd=5, fg="black", font=('ariel', 13, 'bold'), width=14,
                            text="ADD", bg="powder blue")
            btnAdd.place(y=250, x=159)

            # ------------------------------------------ TO DELETE ITEM ---------------------------------------------
            # --------------------------------- ITEM NAME LABEL AND TEXXTBOX ---------------------------------
            lblDItemName = Label(AdminPage, text="ITEM NAME", font=('ariel', 14, 'bold'))
            lblDItemName.place(y=400, x=20)
            Ditemtxt = StringVar()
            txtDItemName = Entry(AdminPage, font=('ariel', 12, 'bold'), textvariable=Ditemtxt)
            txtDItemName.place(y=403, x=160)

            btnDelete = Button(AdminPage, padx=16, pady=3, bd=5, fg="black", font=('ariel', 13, 'bold'), width=14,
                               text="DELETE", bg="powder blue")
            btnDelete.place(y=450, x=159)

            btnShow = Button(AdminPage, padx=16, pady=3, bd=5, fg="black", font=('ariel', 16, 'bold'), width=10,
                             text="SHOW", bg="powder blue", command=Show)
            btnShow.place(y=530, x=787)

            AdminPage.mainloop()

    def RMF3(self):

            # ------------------------------------- ****** THIRD FOAM  ****** --------------------------------------------
            self.Select.withdraw()
            Orderfoam = Tk()
            Orderfoam.geometry("1450x650")
            Orderfoam.title("Restaurant Management System")

            Tops = Frame(Orderfoam, width=1450, height=50, relief=SUNKEN)
            Tops.pack(side=TOP)

            # ------------------TIME--------------
            localtime = time.asctime(time.localtime(time.time()))

            # -----------------INFO TOP------------
            lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", fg="steel blue",
                            bd=10,
                            anchor='w')
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(Tops, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)

            s = ttk.Style()
            s.configure('TNotebook.Tab', font=('URW Gothic L', '14', 'bold'), width=15, anchor='center')
            # s.layout('TNotebook.Tab', [])
            TAB_CONTROL = ttk.Notebook(Orderfoam)

            TAB1 = Frame(TAB_CONTROL)
            TAB_CONTROL.add(TAB1, text='MAIN')

            TAB2 = Frame(TAB_CONTROL)
            TAB_CONTROL.add(TAB2, text='ORDER')
            #TAB_CONTROL.tab(1, state="disabled")

            TAB3 = Frame(TAB_CONTROL)
            TAB_CONTROL.add(TAB3, text='BILL')
            #TAB_CONTROL.tab(2, state="disabled")
            TAB_CONTROL.pack(expand=1, fill="both")

            def yourorder():

                treeview = tree

                if (text.get() == 0) and (cbbriyani.get() == 0):
                    TAB_CONTROL.select(0)
                    messagebox.showerror(" Error !", " PLACE YOUR ORDER ")


                if (text.get() == 1):
                    TAB_CONTROL.tab(1, state="normal")
                    TAB_CONTROL.select(1)
                    TAB_CONTROL.tab(0, state="disabled")
                    treeview.insert('', 'end', text=" Pizza ")#, value=(pizzatxt.get()))

                if (cbbriyani.get() == 1):
                    TAB_CONTROL.tab(1, state="normal")
                    TAB_CONTROL.select(1)
                    TAB_CONTROL.tab(0, state="disabled")
                    treeview.insert('', 'end', text=" Briyani ")#, value=(txtBriyani.get(), " 20 Rs "))


            # ******************************* MAIN TAB *********************************

            btnconfirm = Button(TAB1, padx=16, pady=3, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
                                text="CONFIRM", bg="powder blue", command=yourorder)
            btnconfirm.place(y=455, x=1080)

            # ----------------------------- LABEL FRAME 1 ------------------------------
            price = LabelFrame(TAB1, font=('aria', 18, 'bold'), text=" PRICE ", width=300, height=450)
            price.place(y=5, x=5)

            # ------------------------- INSIDE LABEL FRAME 1 ---------------------------
            stxt = StringVar()
            searchtxt = Entry(price, font=('ariel', 12, 'bold'), textvariable=stxt)
            ssearch = stxt.get()
            searchtxt.place(y=10, x=5)

            searchbtn = Button(price, text="Search", font=('ariel', 8, 'bold'), width=11)  # , command=show)
            searchbtn.place(y=8, x=200)

            # ---------------------------- LABEL FRAME 2 -------------------------------

            item = LabelFrame(TAB1, font=('aria', 18, 'bold'), text=" ITEMS ", width=968, height=450)
            item.place(y=5, x=308)

            # ------------------------- INSIDE LABEL FRAME 2 ---------------------------
            # ***********************************Burgers**************************************
            text = IntVar()

            cbburger = Label(item, text="-:Burgers:-", font=('ariel', 14, 'bold'))
            cbburger.place(y=10, x=60)
            cbburger.pack_forget()
            txtburger = StringVar()

            # ***********************************Biryani**************************************
            cbbriyani = IntVar()

            cbBriyani = Label(item, text="-:Biryani:-", font=('ariel', 14, 'bold'))
            cbBriyani.place(y=10, x=310)

            # ***********************************BBQ**************************************

            cbbbq = IntVar()

            cbbbq = Label(item, text="-:Bar B Q:-", font=('ariel', 14, 'bold'))
            cbbbq.place(y=10, x=570)

            # ***********************************Drinks**************************************

            cbdrinks = IntVar()

            cbdrinks = Label(item, text="-:Drinks:-", font=('ariel', 14, 'bold'))
            cbdrinks.place(y=10, x=820)

            # ***********************************sub_headings**************************************
            # ***********************************c_burger**************************************
            c_b = IntVar()
            c_b = Checkbutton(item, text="Chicken Burger", font=('ariel', 11, 'bold'), variable=c_b, onvalue=1,
                              offvalue=0)
            c_b.place(y=50, x=10)
            c_b.pack_forget()
            c_bur = StringVar()
            c_bur = Entry(item, font=('ariel', 10, 'bold'), textvariable=c_b, width=5)
            c_bur.place(y=50, x=180)
            # ***********************************z_burger**************************************
            z_b = IntVar()
            z_b = Checkbutton(item, text="Zinger Burger", font=('ariel', 11, 'bold'), variable=z_b, onvalue=1,
                              offvalue=0)
            z_b.place(y=90, x=10)
            z_b.pack_forget()
            z_bur = StringVar()
            z_bur = Entry(item, font=('ariel', 10, 'bold'), textvariable=z_bur, width=5)
            z_bur.place(y=90, x=180)
            # ***********************************a_burger**************************************
            a_b = IntVar()
            a_b = Checkbutton(item, text="Anday Wala Burger", font=('ariel', 11, 'bold'), variable=a_b, onvalue=1,
                              offvalue=0)
            a_b.place(y=130, x=10)
            a_b.pack_forget()
            a_bur = StringVar()
            a_bur = Entry(item, font=('ariel', 10, 'bold'), textvariable=a_bur, width=5)
            a_bur.place(y=130, x=180)
            # ***********************************chicken_biryani**************************************
            c_bi = IntVar()
            c_bi = Checkbutton(item, text="Chicken Biryani", font=('ariel', 11, 'bold'), variable=c_bi, onvalue=1,
                               offvalue=0)
            c_bi.place(y=50, x=270)
            c_bi.pack_forget()
            c_bir = StringVar()
            c_bir = Entry(item, font=('ariel', 10, 'bold'), textvariable=c_bir, width=5)
            c_bir.place(y=50, x=420)
            # ***********************************Mutton_biryani**************************************
            m_bi = IntVar()
            m_bi = Checkbutton(item, text="Mutton Biryani", font=('ariel', 11, 'bold'), variable=m_bi, onvalue=1,
                               offvalue=0)
            m_bi.place(y=90, x=270)
            m_bi.pack_forget()
            m_bir= StringVar()
            m_bir = Entry(item, font=('ariel', 10, 'bold'), textvariable=m_bir, width=5)
            m_bir.place(y=90, x=420)
            # ***********************************Pulaao**************************************
            p = IntVar()
            p = Checkbutton(item, text="Pulao", font=('ariel', 11, 'bold'), variable=p, onvalue=1,
                            offvalue=0)
            p.place(y=130, x=270)
            p.pack_forget()
            pul = StringVar()
            pul = Entry(item, font=('ariel', 10, 'bold'), textvariable=pul, width=5)
            pul.place(y=130, x=420)
            # ***********************************Tikka**************************************
            t = IntVar()
            t = Checkbutton(item, text="Chicken Tikka", font=('ariel', 11, 'bold'), variable=t, onvalue=1,
                            offvalue=0)
            t.place(y=50, x=530)
            t.pack_forget()
            ti = StringVar()
            ti = Entry(item, font=('ariel', 10, 'bold'), textvariable=ti, width=5)
            ti.place(y=50, x=670)
            # ***********************************Chicken Roll**************************************
            c_r = IntVar()
            c_r = Checkbutton(item, text="Chicken Roll", font=('ariel', 11, 'bold'), variable=c_r, onvalue=1,
                              offvalue=0)
            c_r.place(y=90, x=530)
            c_r.pack_forget()
            c_ro = StringVar()
            c_ro = Entry(item, font=('ariel', 10, 'bold'), textvariable=c_ro, width=5)
            c_ro.place(y=90, x=670)
            # ***********************************Boti Roll**************************************
            b_r = IntVar()
            b_r = Checkbutton(item, text="Beef Roll", font=('ariel', 11, 'bold'), variable=p, onvalue=1,
                            offvalue=0)
            b_r.place(y=130, x=530)
            b_r.pack_forget()
            b_ro = StringVar()
            b_ro = Entry(item, font=('ariel', 10, 'bold'), textvariable=b_ro, width=5)
            b_ro.place(y=130, x=670)

            # ***********************************Pepsi**************************************
            pepsi = IntVar()
            pepsi = Checkbutton(item, text="Pepsi", font=('ariel', 11, 'bold'), variable=pepsi, onvalue=1,
                                offvalue=0)
            pepsi.place(y=50, x=780)
            pepsi.pack_forget()
            pep = StringVar()
            pep = Entry(item, font=('ariel', 10, 'bold'), textvariable=pep,width=5)
            pep.place(y=50, x=920)
            # ***********************************Dew**************************************
            dew = IntVar()
            dew = Checkbutton(item, text="DEW", font=('ariel', 11, 'bold'), variable=c_r, onvalue=1,
                              offvalue=0)
            dew.place(y=90, x=780)
            dew.pack_forget()
            d = StringVar()
            d = Entry(item, font=('ariel', 10, 'bold'),textvariable=d, width=5)
            d.place(y=90, x=920)
            # ***********************************7up**************************************
            s_p = IntVar()
            s_p = Checkbutton(item, text="7 Up", font=('ariel', 11, 'bold'), variable=p, onvalue=1,
                            offvalue=0)
            s_p.place(y=130, x=780)
            s_p.pack_forget()
            s = StringVar()
            s = Entry(item, font=('ariel', 10, 'bold'),textvariable=s, width=5)
            s.place(y=130, x=920)
            # ***********************************Water Bottle**************************************
            w_b= IntVar()
            w_b = Checkbutton(item, text="Water Bottle", font=('ariel', 11, 'bold'), variable=t, onvalue=1,
                            offvalue=0)
            w_b.place(y=170, x=780)
            w_b.pack_forget()
            bt = StringVar()
            bt = Entry(item, font=('ariel', 10, 'bold'), textvariable=bt,width=5)
            bt.place(y=170, x=920)

            # ******************************* ORDER TAB *********************************
            style = ttk.Style()
            style.configure("Treeview", rowheight=35, font=('Calibri', 18, 'bold'))
            style.configure("Treeview.Heading", font=('Calibri', 16, 'bold'))  # Modify the font of the headings
            tree = ttk.Treeview(TAB2)

            tree["columns"] = ("one", "two", "three")
            tree.config(height=50)
            tree.place(y=10, x=10)

            tree.column("#0", width=200, minwidth=200, stretch=NO)
            tree.column("one", width=120, minwidth=100, stretch=NO)
            tree.column("two", width=100, minwidth=50)

            tree.heading("#0", text=" ITEM ", anchor="center")
            tree.heading("one", text=" QUANTITY ", anchor="center")
            tree.heading("two", text=" PRICE ", anchor="center")

            # ******************************* BILL TAB *********************************

            Orderfoam.mainloop()
root = Tk()
obj = Login_system(root)
root.mainloop()
