from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="white", fg="Black", relief=GROOVE)
        title.pack(fill=X)
        
    # ================variables=======================
    
        self.tomato_rice = IntVar()
        self.veg_briyanni = IntVar()
        self.lemon_rice = IntVar()
        self.chikken_briyanni = IntVar()
        self.karu = IntVar()
        self.sambar = IntVar()
        
    # ============grocery==============================
       
        self.idlee = IntVar()
        self.dosa = IntVar()
        self.chappathi = IntVar()
        self.pongal = IntVar()
        self.seva = IntVar()
        self.oothappam = IntVar()
        
     #=============coldDtinks=============================
        
        self.coffee = IntVar()
        self.masala_coffee = IntVar()
        self.malli_coffee = IntVar()
        self.milk_shake = IntVar()
        self.honey_milk = IntVar()
        self.sukku_coffee = IntVar()
        
    # ==============Total product pidlee================
    
        self.variety_rice = StringVar()
        self.tiffan = StringVar()
        self.drinks = StringVar()
        
    # ==============Customer==========================
    
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
    # ===============Tax================================
    
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        
    # =============customer retail details======================
    
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#badc57", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Medical====================================
    
        F2 = LabelFrame(self.root, text="Vareity idlees", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F2.place(x=5, y=180, width=325, height=380)

        tomato_rice_lbl = Label(F2, text="Lemon rice", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        tomato_rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        tomato_rice_txt = Entry(F2, width=10, textvariable=self.tomato_rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        tomato_rice_txt.grid(row=0, column=1, padx=10, pady=10)

        veg_briyanni_lbl = Label(F2, text="Tomato rice", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        veg_briyanni_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        veg_briyanni_txt = Entry(F2, width=10, textvariable=self.veg_briyanni, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        veg_briyanni_txt.grid(row=1, column=1, padx=10, pady=10)

        lemon_rice_lbl = Label(F2, text="Veg Briyanni", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        lemon_rice_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        lemon_rice_txt = Entry(F2, width=10, textvariable=self.lemon_rice, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        lemon_rice_txt.grid(row=2, column=1, padx=10, pady=10)

        chikken_briyanni_lbl = Label(F2, text="Chikken Briyanni", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        chikken_briyanni_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        chikken_briyanni_txt = Entry(F2, width=10, textvariable=self.chikken_briyanni, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        chikken_briyanni_txt.grid(row=3, column=1, padx=10, pady=10)

        karu_lbl = Label(F2, text="Karuveplai Sadham", font =('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
        karu_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        karu_txt = Entry(F2, width=10, textvariable=self.karu, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        karu_txt.grid(row=4, column=1, padx=10, pady=10)

        sambar_lbl = Label(F2, text="Sambar Sadham", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sambar_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        sambar_txt = Entry(F2, width=10, textvariable=self.sambar, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sambar_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
    
        F3 = LabelFrame(self.root, text="Tiffan Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F3.place(x=340, y=180, width=325, height=380)

        idlee_lbl = Label(F3, text="Idly", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        idlee_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        idlee_txt = Entry(F3, width=10, textvariable=self.idlee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        idlee_txt.grid(row=0, column=1, padx=10, pady=10)

        dosa_lbl = Label(F3, text="Dosa", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        dosa_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        dosa_txt = Entry(F3, width=10, textvariable=self.dosa, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        dosa_txt.grid(row=1, column=1, padx=10, pady=10)

        chappathi_lbl = Label(F3, text="Chappathi", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        chappathi_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        chappathi_txt = Entry(F3, width=10, textvariable=self.chappathi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        chappathi_txt.grid(row=2, column=1, padx=10, pady=10)

        pongal_lbl = Label(F3, text="Pongal", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        pongal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        pongal_txt = Entry(F3, width=10, textvariable=self.pongal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        pongal_txt.grid(row=3, column=1, padx=10, pady=10)

        seva_lbl = Label(F3, text="Seva", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        seva_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        seva_txt = Entry(F3, width=10, textvariable=self.seva, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        seva_txt.grid(row=4, column=1, padx=10, pady=10)

        oothappam_lbl = Label(F3, text="Oothappam", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        oothappam_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        oothappam_txt = Entry(F3, width=10, textvariable=self.oothappam, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        oothappam_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
    
        F4 = LabelFrame(self.root, text="Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F4.place(x=670, y=180, width=325, height=380)

        coffee_lbl = Label(F4, text="Coffee", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        coffee_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        coffee_txt = Entry(F4, width=10, textvariable=self.coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coffee_txt.grid(row=0, column=1, padx=10, pady=10)

        masala_coffee_lbl = Label(F4, text="Masala Coffee", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        masala_coffee_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        masala_coffee_txt = Entry(F4, width=10, textvariable=self.masala_coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        masala_coffee_txt.grid(row=1, column=1, padx=10, pady=10)

        malli_coffee_lbl = Label(F4, text="Milk shake", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        malli_coffee_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        chappathi_txt = Entry(F4, width=10, textvariable=self.malli_coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        chappathi_txt.grid(row=2, column=1, padx=10, pady=10)

        milk_shake_lbl = Label(F4, text="Honey milk", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        milk_shake_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        milk_shake_txt = Entry(F4, width=10, textvariable=self.milk_shake, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        milk_shake_txt.grid(row=3, column=1, padx=10, pady=10)

        honey_milk_lbl = Label(F4, text="Sukku Coffee", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        honey_milk_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        honey_milk_txt = Entry(F4, width=10, textvariable=self.honey_milk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        honey_milk_txt.grid(row=4, column=1, padx=10, pady=10)

        sukku_coffee_lbl = Label(F4, text="Malli Coffee", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sukku_coffee_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        sukku_coffee_txt = Entry(F4, width=10, textvariable=self.sukku_coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sukku_coffee_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
    
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
    
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#badc57")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Variety idlees", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.variety_rice, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Tiffan items", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.tiffan, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Drinks", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.drinks, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="GST", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="SGST", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="GST", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
    
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================

    def total(self):
        self.m_h_g_p = self.lemon_rice.get()*40
        self.m_s_p = self.tomato_rice.get()*40
        self.m_m_p = self.veg_briyanni.get()*40
        self.m_d_p = self.chikken_briyanni.get()*40
        self.m_n_p = self.karu.get()*40
        self.m_t_g_p = self.sambar.get()*40
        self.total_variety_rice = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.variety_rice.set("Rs. "+str(self.total_variety_rice))
        self.c_tax = round((self.total_variety_rice*0.18), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.idlee.get()*20
        self.g_f_o_p = self.dosa.get()*20
        self.g_w_p = self.chappathi.get()*20
        self.g_d_p = self.pongal.get()*20
        self.g_f_p = self.seva.get()*20
        self.g_m_p = self.oothappam.get()*20
        self.total_tiffan = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)

        self.tiffan.set("Rs. " + str(self.total_tiffan))
        self.g_tax = round((self.total_tiffan*0.18), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.coffee.get()*10
        self.c_d_l_p = self.masala_coffee.get()*10
        self.c_d_m_p = self.malli_coffee.get()*10
        self.c_d_c_p = self.milk_shake.get()*10
        self.c_d_f_p = self.honey_milk.get()*10
        self.c_m_d = self.sukku_coffee.get()*10
        self.total_drinks = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.drinks.set("Rs. "+str(self.total_drinks))
        self.c_d_tax = round((self.total_drinks * 0.18), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_variety_rice+self.total_tiffan+self.total_drinks+self.c_tax+self.g_tax+self.c_d_tax)

#==============welcome-bill==============================

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Saptingala!")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number:{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================

    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.variety_rice.get() == "Rs. 0.0" and self.tiffan.get() == "Rs. 0.0" and self.drinks.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            
    # ============medical===========================
    
        if self.tomato_rice.get() != 0:
            self.txtarea.insert(END, f"\n Lemon rice\t\t{self.tomato_rice.get()}\t\t{self.m_s_p}")
        if self.veg_briyanni.get() != 0:
            self.txtarea.insert(END, f"\n Tomato rice\t\t{self.veg_briyanni.get()}\t\t{self.m_m_p}")
        if self.lemon_rice.get() != 0:
            self.txtarea.insert(END, f"\n Veg briyanni\t\t{self.lemon_rice.get()}\t\t{self.m_h_g_p}")
        if self.chikken_briyanni.get() != 0:
            self.txtarea.insert(END, f"\n Chikken briyanni\t\t{self.chikken_briyanni.get()}\t\t{self.m_d_p}")
        if self.karu.get() != 0:
            self.txtarea.insert(END, f"\n Karuveppilai sadham\t\t{self.karu.get()}\t\t{self.m_n_p}")
        if self.sambar.get() != 0:
            self.txtarea.insert(END , f"\n Sambar Sadham\t\t{self.tomato_rice.get()}\t\t{self.m_t_g_p}")
            
    # ==============Grocery============================
    
        if self.idlee.get() != 0:
            self.txtarea.insert(END, f"\n idlee\t\t{self.idlee.get()}\t\t{self.g_r_p}")
        if self.dosa.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.dosa.get()}\t\t{self.g_f_o_p}")
        if self.chappathi.get() != 0:
            self.txtarea.insert(END, f"\n chappathi\t\t{self.chappathi.get()}\t\t{self.g_w_p}")
        if self.pongal.get() != 0:
            self.txtarea.insert(END, f"\n pongal\t\t{self.pongal.get()}\t\t{self.g_d_p}")
        if self.seva.get() != 0:
            self.txtarea.insert(END, f"\n seva\t\t{self.seva.get()}\t\t{self.g_f_p}")
        if self.oothappam.get() != 0:
            self.txtarea.insert(END, f"\n oothappam\t\t{self.oothappam.get()}\t\t{self.g_m_p}")
            
        #================ColdDrinks==========================
        
        if self.coffee.get() != 0:
            self.txtarea.insert(END, f"\n coffee\t\t{self.coffee.get()}\t\t{self.c_d_s_p}")
        if self.masala_coffee.get() != 0:
            self.txtarea.insert(END, f"\n tomato_rice\t\t{self.masala_coffee.get()}\t\t{self.c_d_l_p}")
        if self.malli_coffee.get() != 0:
            self.txtarea.insert(END, f"\n malli_coffee\t\t{self.malli_coffee.get()}\t\t{self.c_d_m_p}")
        if self.milk_shake.get() != 0:
            self.txtarea.insert(END, f"\n chikken_briyanni\t\t{self.milk_shake.get()}\t\t{self.c_d_c_p}")
        if self.honey_milk.get() != 0:
            self.txtarea.insert(END, f"\n honey_milk\t\t{self.karu.get()}\t\t{self.c_d_f_p}")
        if self.sukku_coffee.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.tomato_rice.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
            
        # ===============taxes==============================
        
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n GST\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n SGST\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n CGST\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("./bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"./bills/{i}", "r")
                self.txtarea.delete("1.0", END)

                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.tomato_rice.set(0)
            self.veg_briyanni.set(0)
            self.lemon_rice.set(0)
            self.chikken_briyanni.set(0)
            self.karu.set(0)
            self.sambar.set(0)
            
    # ============grocery==============================
    
            self.idlee.set(0)
            self.dosa.set(0)
            self.chappathi.set(0)
            self.pongal.set(0)
            self.seva.set(0)
            self.oothappam.set(0)
            
    # =============coldDrinks=============================
    
            self.coffee.set(0)
            self.masala_coffee.set(0)
            self.malli_coffee.set(0)
            self.milk_shake.set(0)
            self.honey_milk.set(0)
            self.sukku_coffee.set(0)
            
    # ====================taxes================================
    
            self.variety_rice.set("")
            self.tiffan.set("")
            self.drinks.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()