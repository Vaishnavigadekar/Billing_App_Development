#!/usr/bin/env python
# coding: utf-8

# # <span style ='color:Black'> BILL DEVLOPMENT APP </span>

# ![Screenshot%20%281%29.png](attachment:Screenshot%20%281%29.png)

# ## Objective:

# - The main objective of the Online Billing System is to manage the details of Bills,Payment,Customer name and ID , total items. It manages all the information about Bills, Cash, Delivery, Bills.
# 
# - Providing different keys with functions such as Total, Generate bill , clear and exits.
# 
# - Learning correct sequencial order while developing interface of Dashboard.
# 

# In[3]:


from tkinter import*
import random
import os
from tkinter import messagebox


# ## tkinter :
# Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.

# In[4]:


class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('coders redy vaish')
        bg_color ='#f20c2b'
        title = Label(self.root,text= 'Coders ready dashbord, Ready to shop!!', font= ('times new roman',30 ,'bold'), pady = 2, bd = 12, bg = "#f20c2b",fg='Black',relief=GROOVE)
        title.pack(fill = X)
        
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.detol = IntVar()
        self.disprin = IntVar()
        self.thermal_gun = IntVar()
                      
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.pulses = IntVar()
        self.flour = IntVar()
        self.sugar = IntVar()
                      
        self.coke = IntVar()
        self.sprite = IntVar()
        self.limca = IntVar()
        self.fanta = IntVar()
        self.mazza = IntVar()
        self.mountain_dew = IntVar()
                      
        self.medical_price = StringVar()
        self.grocery_price = StringVar()              
        self.cold_drink_price = StringVar()              
                      
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill_no = StringVar()             
        x = random.randint(1000,9999)              
        self.c_bill_no.set(str(x))            #45   
        self.search_bill = StringVar()              
        
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()
        
        F1 = LabelFrame(self.root, text = 'customer details', font=('times new roman', 15, 'bold'),bd =10, fg ='Black', bg = '#f20c2b') #52             
        F1.place(x= 0, y =80,relwidth=1)
                      
        cname_lbl = Label(F1, text = 'customer name:', bg = bg_color, font=('times new roman',15,'bold'))
        cname_lbl.grid(row =0, column = 0,pady=20,padx=5)             
        cname_text = Entry(F1, width=15,textvariable=self.c_name, font= 'arial 15', bd =7,relief = GROOVE)              
        cname_text.grid(row =0, column = 1,pady=5,padx=10)  
                      
        cphn_lbl = Label(F1, text = 'customer phone no:', bg = bg_color, font=('times new roman',15,'bold'))
        cphn_lbl.grid(row =0, column = 2,pady=20,padx=5)             
        cphn_text = Entry(F1, width=15,textvariable=self.c_phone, font= 'arial 15', bd =7,relief = GROOVE)              
        cphn_text.grid(row =0, column = 3,pady=5,padx=10)
        
        c_bill_lbl =  Label(F1, text = 'bill number:', bg ='#f20c2b', font=('times new roman',15,'bold'))
        c_bill_lbl.grid(row =0, column =4,pady=20,padx=5)              
        c_bill_text =Entry(F1, width=15,textvariable=self.search_bill, font= 'arial 15', bd =7,relief = GROOVE)              
        c_bill_text.grid(row =0, column = 5,pady=5,padx=10) 
                      
        bill_btn = Button(F1, text='search',command= self.find_bill,width=10, bd=7,font=('arial',12,'bold'), relief=GROOVE)     #70
        bill_btn.grid(row =0, column = 6,pady=5,padx=10)              
                      
        F2=LabelFrame(self.root, text = 'medical purpose', font=('times new roman', 16, 'bold'),bd =10, fg ='Black', bg = '#f20c2b')   
        F2.place(x= 5, y =180,width=325, height=380)
                       
        sanitizer_lbl =  Label(F2, text = 'sanitizer:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        sanitizer_lbl.grid(row =0, column =0,pady=10,padx=10, sticky='w')              
        sanitizer_text =Entry(F2, width=10,textvariable=self.sanitizer,font=('times new roman',15,'bold'),bd=5, relief = GROOVE)              
        sanitizer_text.grid(row =0, column = 1,pady=10,padx=10)
                      
        mask_lbl =  Label(F2, text = 'mask:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        mask_lbl.grid(row =1, column =0,pady=10,padx=10, sticky='w')              
        mask_text =Entry(F2, width=10,textvariable=self.mask,font=('times new roman',15,'bold'),bd=5, relief = GROOVE)              
        mask_text.grid(row =1, column = 1,pady=10,padx=10)              
                      
        hand_gloves_lbl =  Label(F2, text = 'hand gloves:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')       #86
        hand_gloves_lbl.grid(row =2, column =0,pady=10,padx=10, sticky='w')              
        hand_gloves_text =Entry(F2, width=10,textvariable=self.hand_gloves,font=('times new roman',15,'bold'),bd=5, relief = GROOVE)              
        hand_gloves_text.grid(row =2, column = 1,pady=10,padx=10)              
                      
        detol_lbl =  Label(F2, text = 'detol:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        detol_lbl.grid(row =3, column =0,pady=10,padx=10, sticky='w')              
        detol_text =Entry(F2, width=10,textvariable=self.detol,font=('times new roman',15,'bold'),bd=5, relief = GROOVE)              
        detol_text.grid(row =3, column = 1,pady=10,padx=10)              
                      
        disprin_lbl =  Label(F2, text = 'disprin:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        disprin_lbl.grid(row =4, column =0,pady=10,padx=10, sticky='w')              
        disprin_text =Entry(F2, width=10,textvariable=self.disprin,font=('times new roman',15,'bold'),bd=5, relief = GROOVE)              
        disprin_text.grid(row =4, column = 1,pady=10,padx=10)              
                      
        thermal_gun_lbl =  Label(F2, text = 'thermal gun:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        thermal_gun_lbl.grid(row =5, column =0,pady=10,padx=10, sticky='w')              
        thermal_gun_text =Entry(F2, width=10,textvariable=self.thermal_gun,font=('times new roman',15,'bold'),bd=5, relief = GROOVE)              
        thermal_gun_text.grid(row =5, column = 1,pady=10,padx=10)              
                      
        
        F3=LabelFrame(self.root, text = 'grocery purpose', font=('times new roman', 16, 'bold'),bd =10, fg ='Black', bg = '#f20c2b')   
        F3.place(x= 340, y =180,width=325, height=380)    #108
                       
        rice_lbl =  Label(F3, text = 'rice:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        rice_lbl.grid(row =0, column =0,pady=10,padx=10, sticky='w')              
        rice_text =Entry(F3, width=10,textvariable=self.rice,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        rice_text.grid(row =0, column = 1,pady=10,padx=10)
                      
        food_oil_lbl =  Label(F3, text = 'food oil:',font=('times new roman',15,'bold'),bg="#f20c2b", fg='Black')
        food_oil_lbl.grid(row =1, column =0,pady=10,padx=10, sticky='w')              
        food_oil_text =Entry(F3, width=10,textvariable=self.food_oil,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        food_oil_text.grid(row =1, column = 1,pady=10,padx=10)              
                      
        wheat_lbl =  Label(F3, text = 'wheat:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        wheat_lbl.grid(row =2, column =0,pady=10,padx=10, sticky='w')              
        wheat_text =Entry(F3, width=10,textvariable=self.wheat,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        wheat_text.grid(row =2, column = 1,pady=10,padx=10)              
                      
        flour_lbl =  Label(F3, text = 'flour:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        flour_lbl.grid(row =3, column =0,pady=10,padx=10, sticky='w')              
        flour_text =Entry(F3, width=10,textvariable=self.flour,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        flour_text.grid(row =3, column = 1,pady=10,padx=10)              
                      
        sugar_lbl =  Label(F3, text = 'sugar:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        sugar_lbl.grid(row =4, column =0,pady=10,padx=10, sticky='w')              
        sugar_text =Entry(F3, width=10,textvariable=self.sugar,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        sugar_text.grid(row =4, column = 1,pady=10,padx=10)              
                      
        pulses_lbl =  Label(F3, text = 'pulses:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        pulses_lbl.grid(row =5, column =0,pady=10,padx=10, sticky='w')              
        pulses_text =Entry(F3, width=10,textvariable=self.pulses,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        pulses_text.grid(row =5, column = 1,pady=10,padx=10)   
                      
                      
        F4=LabelFrame(self.root, text = 'cold drink', font=('times new roman', 16, 'bold'),bd =10, fg ='Black', bg = '#f20c2b')   
        F4.place(x= 670, y =180,width=325, height=380)
                       
        coke_lbl =  Label(F4, text = 'coke:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        coke_lbl.grid(row =0, column =0,pady=10,padx=10, sticky='w')              
        coke_text =Entry(F4, width=10,textvariable=self.coke,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        coke_text.grid(row =0, column = 1,pady=10,padx=10)
                      
        sprite_lbl =  Label(F4, text = 'sprite:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        sprite_lbl.grid(row =1, column =0,pady=10,padx=10, sticky='w')              
        sprite_text =Entry(F4, width=10,textvariable=self.sprite,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        sprite_text.grid(row =1, column = 1,pady=10,padx=10)              
                      
        limca_lbl =  Label(F4, text = 'limka:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        limca_lbl.grid(row =2, column =0,pady=10,padx=10, sticky='w')              
        limca_text =Entry(F4, width=10,textvariable=self.limca,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        limca_text.grid(row =2, column = 1,pady=10,padx=10)              
                      
        fanta_lbl =  Label(F4, text = 'fanta:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        fanta_lbl.grid(row =3, column =0,pady=10,padx=10, sticky='w')              
        fanta_text =Entry(F4, width=10,textvariable=self.fanta,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        fanta_text.grid(row =3, column = 1,pady=10,padx=10)              
                      
        mazza_lbl =  Label(F4, text = 'mazza:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        mazza_lbl.grid(row =4, column =0,pady=10,padx=10, sticky='w')              
        mazza_text =Entry(F4, width=10,textvariable=self.mazza,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        mazza_text.grid(row =4, column = 1,pady=10,padx=10)              
                      
        mountain_dew_lbl =  Label(F4, text = 'mountain dew:',font=('times new roman',16,'bold'),bg="#f20c2b", fg='Black')
        mountain_dew_lbl.grid(row =5, column =0,pady=10,padx=10, sticky='w')              
        mountain_dew_text =Entry(F4, width=10,textvariable=self.mountain_dew,font=('times new roman',16,'bold'),bd=5, relief = GROOVE)              
        mountain_dew_text.grid(row =5, column = 1,pady=10,padx=10)   
                      
                                     
        F5=Frame(self.root, bd=10, relief= GROOVE)      #175        
        F5.place(x=1010, y=180, width = 350,height=380)
        
        bill_title = Label(F5,text='bill deatail area ',font='arial 15 bold',bd=7, relief=GROOVE)
        bill_title.pack(fill=X)                                         #179
        scroll_y = Scrollbar(F5, orient = VERTICAL)
        self.txtarea =  Text(F5,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill =Y)
        scroll_y.config(command = self.txtarea.yview)   #183
        self.txtarea.pack(fill=BOTH,expand=1)
        
        F6=LabelFrame(self.root, text = 'bill detail areas', font=('times new roman', 14, 'bold'),bd =10, fg ='Black', bg = '#f20c2b')   
        F6.place(x= 0, y =560,relwidth=1, height=140)
        
        m1_lbl =  Label(F6, text = 'total medical price',font=('times new roman',14,'bold'),bg="#120103", fg='Red')
        m1_lbl.grid(row =0, column =0,pady=20,padx=1, sticky='w')              
        m1_text =Entry(F6, width=18,textvariable=self.medical_price,font=('arial 10 bold'),bd=7, relief = GROOVE)              
        m1_text.grid(row =0, column = 1,pady=1,padx=18)   
                      
        m2_lbl =  Label(F6, text = 'total grocery price',font=('times new roman',14,'bold'),bg="#120103", fg='Red')
        m2_lbl.grid(row =1, column =0,pady=20,padx=1, sticky='w')              
        m2_text =Entry(F6, width=18,textvariable=self.grocery_price,font=('arial 10 bold'),bd=7, relief = GROOVE)              
        m2_text.grid(row =1, column = 1,pady=1,padx=18)   
                                                   
        m3_lbl =  Label(F6, text ='total cold drink price',font=('times new roman',14,'bold'),bg="#120103", fg='Red')
        m3_lbl.grid(row =2, column =0,pady=20,padx=1, sticky='w')   #200           
        m3_text =Entry(F6, width=18,textvariable=self.cold_drink_price,font=('arial 10 bold'),bd=7, relief = GROOVE)              
        m3_text.grid(row =2, column = 1,pady=1,padx=18)   
                      
        m4_lbl =  Label(F6, text = 'medical tax',font=('times new roman',14,'bold'),bg="#120103", fg='Red')
        m4_lbl.grid(row =0, column =2,pady=20,padx=1, sticky='w')              
        m4_text =Entry(F6, width=18,textvariable=self.medical_tax,font=('arial 10 bold'),bd=7, relief = GROOVE)              
        m4_text.grid(row =0, column = 3,pady=1,padx=18)   
                      
        m5_lbl =  Label(F6, text = 'grocery tax',font=('times new roman',14,'bold'),bg="#120103", fg='Red')
        m5_lbl.grid(row =1, column =2,pady=20,padx=1, sticky='w')              
        m5_text =Entry(F6, width=18,textvariable=self.grocery_tax,font=('arial 10 bold'),bd=7, relief = GROOVE)              
        m5_text.grid(row =1, column = 3,pady=1,padx=18)  
                        
        m6_lbl =  Label(F6, text = 'cold drink tax',font=('times new roman',14,'bold'),bg="#120103", fg='Red')
        m6_lbl.grid(row =2, column =2,pady=20,padx=1, sticky='w')              
        m6_text =Entry(F6, width=18,textvariable=self.cold_drink_tax,font=('arial 10 bold'),bd=7, relief = GROOVE)              
        m6_text.grid(row =2, column = 3,pady=1,padx=18)   
#          /how buttin lock like and how they are run     


        btn_f = Frame(F6,bd = 7,relief=GROOVE)       #219
        btn_f.place(x=760,width=580, height=105)
        
        total_btn = Button(btn_f, command=self.total, text='total',bg='#f20c2b',bd=2,fg='black',pady=12,width=12,font='arial 13 bold')
        total_btn.grid(row=0,column=0,padx=5,pady=5)   #223
                        
        generatebill_btn = Button(btn_f, command=self.bill_area, text='genrate bill',bg='#f20c2b',bd=2,fg='black',pady=12,width=12,font='arial 13 bold')
        generatebill_btn.grid(row=0,column=1,padx=5,pady=5)                
                        
        clear_btn = Button(btn_f, command=self.clear_data, text='clear',bg='#f20c2b',bd=2,fg='black',pady=12,width=12,font='arial 13 bold')
        clear_btn.grid(row=0,column=2,padx=5,pady=5)                
                        
        exit_btn = Button(btn_f, command=self.exit_app, text='exit',bg='#f20c2b',bd=2,fg='black',pady=12,width=12,font='arial 13 bold')
        exit_btn.grid(row=0,column=3,padx=5,pady=5) 
        self.welcome()
        
    def total(self):
        self.m_s_p = self.sanitizer.get()*20
        self.m_m_p = self.mask.get()*5
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_de_p = self.detol.get()*30
        self.m_d_p = self.disprin.get()*2
        self.m_t_g_p = self.thermal_gun.get()*150
            
        self.total_medical_price=float(self.m_s_p+self.m_m_p+self.m_h_g_p+self.m_de_p+self.m_d_p+self.m_t_g_p)
        
        self.medical_price.set('Rs.'+str(self.total_medical_price))                     
        self.m_tax = round((self.total_medical_price*0.05),2)            
        self.medical_tax.set('RS.'+str(self.m_tax))
                        
        self.g_r_p = self.rice.get()*100
        self.g_f_o_p = self.food_oil.get()*150
        self.g_w_p = self.wheat.get()*25    #250
        self.g_p_p = self.pulses.get()*45
        self.g_f_p = self.flour.get()*100
        self.g_s_p = self.sugar.get()*60
            
        self.total_grocery_price=float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_p_p+self.g_f_p+self.g_s_p)
        self.grocery_price.set('Rs.'+str(self.total_grocery_price))
                                        
        self.g_tax = round((self.total_grocery_price*0.05),2)            
        self.grocery_tax.set('RS.'+str(self.g_tax))
                                    
        self.c_d_c_p = self.coke.get()*140
        self.c_d_s_p = self.sprite.get()*140
        self.c_d_l_p = self.limca.get()*140
        self.c_d_f_p = self.fanta.get()*40
        self.c_d_m_p = self.mazza.get()*140
        self.c_d_m_d_p = self.mountain_dew.get()*40
            
        self.total_cold_drink_price=float(self.c_d_c_p+self.c_d_s_p+self.c_d_l_p+self.c_d_f_p+self.c_d_m_p+self.c_d_m_d_p)
        self.cold_drink_price.set('Rs.'+str(self.total_cold_drink_price))
                                        
        self.c_d_tax = round((self.total_cold_drink_price*0.1),2)            
        self.cold_drink_tax.set('RS.'+str(self.c_d_tax))            
                        
        self.total_bill = float(self.c_d_tax+self.total_cold_drink_price+self.g_tax+self.total_grocery_price+self.m_tax+self.total_medical_price)            
            
    def welcome(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, '\twelcome')
        self.txtarea.insert(END, f'\nbill no;{self.c_bill_no.get()}')    #279
        self.txtarea.insert(END, f'\ncustomer name;{self.c_name.get()}')
        self.txtarea.insert(END, f'\nphone no;{self.c_phone.get()}')
        self.txtarea.insert(END, f'\n=============================')
        self.txtarea.insert(END, f'\nproducts\t\tQTY\t\tprice')
             
                
    def bill_area(self):
        if self.c_name.get()==" " or self.c_phone.get()==' ':
            messagebox.showerror("Error",'customer details are must')
        elif self.medical_price.get() == 'Rs.0.0' and self.grocery_price.get()=='Rs.0.0' and self.cold_drink_price.get() == 'Rs.0.0':
            messagebox.showerror('Error','no product purches')
        else:
            self.welcome()
                    
                    
        if self.sanitizer.get() !=0:
            self.txtarea.insert(END, f'\n sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}')  #296
                    
        if self.mask.get() !=0:
            self.txtarea.insert(END, f'\n mask\t\t{self.mask.get()}\t\t{self.m_m_p}')
                                   
        if self.hand_gloves.get() !=0:
            self.txtarea.insert(END, f'\n hand_gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}')
                
        if self.detol.get() !=0:
            self.txtarea.insert(END, f'\n detol\t\t{self.detol.get()}\t\t{self.m_de_p}')
                    
        if self.disprin.get() !=0:
            self.txtarea.insert(END, f'\n disprin\t\t{self.disprin.get()}\t\t{self.m_d_p}')
                    
                        
        if self.thermal_gun.get() !=0:
            self.txtarea.insert(END, f'\n thermal_gun\t\t{self.thermal_gun.get()}\t\t{self.m_t_g_p}')
                           
                    
        if self.rice.get() !=0:
            self.txtarea.insert(END, f'\n rice\t\t{self.rice.get()}\t\t{self.g_r_p}')
        
                    
        if self.food_oil.get() !=0:
            self.txtarea.insert(END, f'\n food_oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}')
                    
                    
        if self.wheat.get() !=0:
            self.txtarea.insert(END, f'\n wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}')
                    
                    
        if self.pulses.get() !=0:
            self.txtarea.insert(END, f'\n pulses\t\t{self.pulses.get()}\t\t{self.g_p_p}')
                    
                
        if self.flour.get() !=0:
            self.txtarea.insert(END, f'\n flour\t\t{self.flour.get()}\t\t{self.g_f_p}')
                    
                    
        if self.sugar.get() !=0:
            self.txtarea.insert(END, f'\n sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}')
                    
                    
        if self.coke.get() !=0:
            self.txtarea.insert(END, f'\n coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}')
                    
                    
        if self.sprite.get() !=0:
            self.txtarea.insert(END, f'\n sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}')
                    
                    
        if self.limca.get() !=0:
            self.txtarea.insert(END, f'\n limca\t\t{self.limca.get()}\t\t{self.c_d_l_p}')
                    
                    
        if self.fanta.get() !=0:
            self.txtarea.insert(END, f'\n fanta\t\t{self.fanta.get()}\t\t{self.c_d_f_p}')
                    
                        
        if self.mazza.get() !=0:
            self.txtarea.insert(END, f'\n mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}')
                    
                    
        if self.mountain_dew.get() !=0:
            self.txtarea.insert(END, f'\n fanta\t\t{self.mountain_dew.get()}\t\t{self.c_d_m_d_p}')
            self.txtarea.insert(END, f'\n====================================================')
                    
        if self.medical_tax.get() !='0.0':
            self.txtarea.insert(END, f'\n medical_tax\t\t{self.medical_tax.get()}')
                        
                        
        if self.grocery_tax.get() !='0.0':
            self.txtarea.insert(END, f'\n grocery_tax\t\t{self.grocery_tax.get()}')   #368
                        
                                       
        if self.cold_drink_tax.get() !='0.0':
            self.txtarea.insert(END, f'\n cold_drink_tax\t\t{self.cold_drink_tax.get()}')
        
        
            self.txtarea.insert(END, f'\n total bill:\t\t\t{self.total_bill}')   #374
            self.txtarea.insert(END, f'\n=========================================')
            self.save_bill()
                
    def save_bill(self):
            op=messagebox.askyesno('save bill ','do you want to save bill')
            if op>0:
                self.bill_data = self.txtarea.get('1.0', END)
                f1 = open('bill'+str(self.c_bill_no.get())+'.txt','w')
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo('saved',f'bill no:{self.c_bill_no.get()} saved successfully')
                               
            else:
                 return 
#                     391
                    
                    
    def find_bill(self):
        present = 'no'
        for i in os.listdir('bills/'):    #394
            if i.split('.')[0]== self.search_bill.get():
                f1 = open(f'bills/{i}','r')
                self.txtarea.delete('1.0',END)      
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()  
                present = 'yes'    
        if present == 'no':
             messagebox.showerror('Error','invalid bill no') 
                    
    def clear_data(self):
        op = messagebox.askyesno('clear', 'do you really want to clear ?')
        if op>0:
            self.sanitizer.set(0) 
            self.mask.set(0) 
            self.hand_gloves.set(0) 
            self.detol.set(0) 
            self.disprin.set(0) 
            self.thermal_gun.set(0) 
                       
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.pulses.set(0)
            self.flour.set(0)
            self.sugar.set(0)
                                      
            self.coke.set(0)
            self.sprite.set(0)
            self.limca.set(0)
            self.fanta.set(0)
            self.mazza.set(0)
            self.mountain_dew.set(0)
                      
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
                        
            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
    
                    
            self.c_name.set('')   
            self.c_phone.set('')
            
            self.c_bill_no.set('')
            x = random.randint(1000,9999)
            self.c_bill_no.set(str(x))
                        
            self.search_bill.set('')
            self.welcome()
                        
    def exit_app(self):
        op =messagebox.askyesno('exit','do you really want to exit')
        if op>0:
            self.root.destroy()
                
                    
                    
                    
root = Tk()
obj = Bill_App(root)
root.mainloop()        
                        


# ## Results and Analysis:

# - This billing dashboard has been created using tkinter library.
# 
# - This Dashboard facilitated user to enter various information such as Costomer name, Costomer phone number, bill number, column to enter medical products,grocery products and cold drinks.
# 
# - It has bill detail area at bottom of dashboard which reflects Total medical Price , medical tax and option like  total , generate bill ,clear and exit option.
# 
# - Customer Details: This feature takes inputs from user like Customer's Names and phone numbers and also contains a text box in which we can enter previously generated bill numbers and search for their details with the help of the search button.
# 
# - Medical Purpose: This feature takes inputs from user such as several units of medical products i.e Sanitizer, Mask, Hand Gloves, Dettol, Disprine and Thermal Gun.
# 
# - Grocery Items: This feature takes input from user such as several units of Grocery items i.e Rice, Food oil, Wheat, Pulses, Flour, Flour, Suger.
# 
# - Cold Drinks: This feature takes inputs from user such as several units of Cold drinks i.e Coke, Sprite, Lime, Fanta, Mazz and Mountain Dew.
# 
# - Bill detail area: this features list out all items purchased and their quantity with their Prices.
# 
# - Total: This feature allows user to display total amount to be paid by costomer.
# 
# - Generate Bill - this feature allows user to generate bill receipt and also provides an option to save the bill.
# 
# - Clear - This feature allows user to clear the details of one costomer and allows to enter the details of other costomer.
# 
# - Exit: this feature allows the user to exit the dashboard.

# In[ ]:




