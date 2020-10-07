from tkinter import *
from tkinter import messagebox
import datetime
import time
import smtplib

root = Tk()


head_label = Label(root, text="Restaurant Management System",background="lightblue",fg="white",width=42,padx=10,pady=30)
head_label.config(font=("Bold",32))
head_label.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

main_frame_items = LabelFrame(root, text="", padx=5,pady=10,borderwidth=10)
main_frame_items.grid(row=1,column=0,columnspan=3,padx=(15,5),pady=10,sticky=W)

main_frame_price = LabelFrame(root, text="", padx=5,pady=20,borderwidth=10)
main_frame_price.grid(row=2,column=0,columnspan=3,padx=(15,5),pady=10,sticky=W)

main_frame_bill = LabelFrame(root, text="", padx=5,pady=10,borderwidth=10)
main_frame_bill.grid(row=1,rowspan=3,column=3,columnspan=6,padx=(0,5),pady=10,sticky=W+N)

main_frame_option = LabelFrame(root, text="", padx=5,pady=10,borderwidth=10)
main_frame_option.grid(row=1,rowspan=3,column=5,columnspan=7,padx=(5,12),pady=10,sticky=W+N)

drinks_frame = LabelFrame(main_frame_items, text="Drinks",borderwidth=5,padx=30,pady=30)
drinks_frame.grid(row=0,column=0,columnspan=2,padx=5,pady=10)

food_frame = LabelFrame(main_frame_items, text="Food",borderwidth=5,padx=30,pady=30)
food_frame.grid(row=0,column=2,columnspan=4,padx=(15,5),pady=5)

drink_dict = {
        1: ["Lassi",20],
        2: ["Coffee",15],
        3: ["Tea",10],
        4: ["Juice",30],
        5: ["Shakes",50]
}

food_dict = {
        1: ["Roti",10],
        2: ["Dal Makhni",60],
        3: ["Mutter Paneer",80],
        4: ["Paratha",12],
        5: ["Mix Veg",50]
}

#DRINKS check box
drink_check_1 = Label(drinks_frame,text="Lassi",width=10,bg="lightblue")
drink_check_2 = Label(drinks_frame,text="Coffee",width=10,bg="lightblue")
drink_check_3 = Label(drinks_frame,text="Tea",width=10,bg="lightblue")
drink_check_4 = Label(drinks_frame,text="Juice",width=10,bg="lightblue")
drink_check_5 = Label(drinks_frame,text="Shakes",width=10,bg="lightblue")

drink_check_1.grid(row=0,column=0,padx=(0,10),sticky=W)
drink_check_2.grid(row=1,column=0,padx=(0,10),sticky=W)
drink_check_3.grid(row=2,column=0,padx=(0,10),sticky=W)
drink_check_4.grid(row=3,column=0,padx=(0,10),sticky=W)
drink_check_5.grid(row=4,column=0,padx=(0,10),sticky=W)

#DRINKS input
drinks_input_1 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_2 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_3 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_4 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_5 = Entry(drinks_frame,borderwidth=3,width=10)

drinks_input_1.grid(row=0,column=1,sticky=E)
drinks_input_2.grid(row=1,column=1,sticky=E)
drinks_input_3.grid(row=2,column=1,sticky=E)
drinks_input_4.grid(row=3,column=1,sticky=E)
drinks_input_5.grid(row=4,column=1,sticky=E)

#FOOD label
food_check_1 = Label(food_frame,text="Roti",width=10,bg="lightblue")
food_check_2 = Label(food_frame,text="Dal Makhni",width=10,bg="lightblue")
food_check_3 = Label(food_frame,text="Mutter Paneer",width=10,bg="lightblue")
food_check_4 = Label(food_frame,text="Paratha",width=10,bg="lightblue")
food_check_5 = Label(food_frame,text="Mix Veg",width=10,bg="lightblue")

food_check_1.grid(row=0,column=0,padx=(0,10),sticky=W)
food_check_2.grid(row=1,column=0,padx=(0,10),sticky=W)
food_check_3.grid(row=2,column=0,padx=(0,10),sticky=W)
food_check_4.grid(row=3,column=0,padx=(0,10),sticky=W)
food_check_5.grid(row=4,column=0,padx=(0,10),sticky=W)

#FOOD input
food_input_1 = Entry(food_frame,borderwidth=3,width=10)
food_input_2 = Entry(food_frame,borderwidth=3,width=10)
food_input_3 = Entry(food_frame,borderwidth=3,width=10)
food_input_4 = Entry(food_frame,borderwidth=3,width=10)
food_input_5 = Entry(food_frame,borderwidth=3,width=10)

food_input_1.grid(row=0,column=1,sticky=E)
food_input_2.grid(row=1,column=1,sticky=E)
food_input_3.grid(row=2,column=1,sticky=E)
food_input_4.grid(row=3,column=1,sticky=E)
food_input_5.grid(row=4,column=1,sticky=E)

#COST display
cost_drink = Label(main_frame_price,text="COST of Drinks",width=15,pady=5,background="lightblue").grid(row=0,column=0,padx=5)
cost_food = Label(main_frame_price,text="COST of Food",width=15,pady=5,background="lightblue").grid(row=1,column=0,padx=5)
service_charge = Label(main_frame_price,text="Service Charge",width=15,pady=5,background="lightblue").grid(row=2,column=0,padx=5)

cost_drink_input = Entry(main_frame_price,borderwidth=3,width=15)
cost_food_input = Entry(main_frame_price,borderwidth=3,width=15)
service_charge_input = Entry(main_frame_price,borderwidth=3,width=15)

cost_drink_input.grid(row=0,column=1,padx=5,pady=5)
cost_food_input.grid(row=1,column=1,padx=5,pady=5)
service_charge_input.grid(row=2,column=1,padx=5,pady=5)

paid_tax = Label(main_frame_price,text="Paid Tax",width=15,pady=5,background="lightblue").grid(row=0,column=2,padx=(20,5))
sub_total = Label(main_frame_price,text="Sub Total",width=15,pady=5,background="lightblue").grid(row=1,column=2,padx=(20,5))
total_cost = Label(main_frame_price,text="Total Cost",width=15,pady=5,background="lightblue").grid(row=2,column=2,padx=(20,5))

paid_tax_input = Entry(main_frame_price,borderwidth=3,width=15)
sub_total_input = Entry(main_frame_price,borderwidth=3,width=15)
total_cost_input = Entry(main_frame_price,borderwidth=3,width=15)

paid_tax_input.grid(row=0,column=3,padx=5,pady=5)
sub_total_input.grid(row=1,column=3,padx=5,pady=5)
total_cost_input.grid(row=2,column=3,padx=5,pady=5)


#CALCUATOR
cal_input = Entry(main_frame_bill,width=50,borderwidth=5)
cal_input.grid(row=0,column=0,columnspan=5,pady=(0,10),sticky=W)


#CALCULATOR function
def cal(number):
    c = cal_input.get()
    cal_input.delete(0, END)
    cal_input.insert(0, str(c)+str(number))

def button_add():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "add"
    cal_input.delete(0, END)

def button_sub():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "sub"
    cal_input.delete(0, END)

def button_mul():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "mul"
    cal_input.delete(0, END)

def button_div():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "div"
    cal_input.delete(0, END)

def button_equal():
    sec_num = cal_input.get()
    cal_input.delete(0, END)

    if condition == "add":
        cal_input.insert(0, first_num + int(sec_num))   

    if condition == "sub":
        cal_input.insert(0, first_num - int(sec_num))

    if condition == "mul":
        cal_input.insert(0, first_num * int(sec_num)) 

    if condition == "div":
        cal_input.insert(0, first_num / int(sec_num))
    
def button_clear():
    cal_input.delete(0, END)

#Creating buttons for calculator
input_1 = Button(main_frame_bill,text="1",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(1))
input_2 = Button(main_frame_bill,text="2",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(2))
input_3 = Button(main_frame_bill,text="3",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(3))
input_4 = Button(main_frame_bill,text="4",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(4))
input_5 = Button(main_frame_bill,text="5",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(5))
input_6 = Button(main_frame_bill,text="6",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(6))
input_7 = Button(main_frame_bill,text="7",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(7))
input_8 = Button(main_frame_bill,text="8",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(8))
input_9 = Button(main_frame_bill,text="9",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(9))
input_0 = Button(main_frame_bill,text="0",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(0))

input_add = Button(main_frame_bill,text="+",padx=31,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_add)
input_sub = Button(main_frame_bill,text="-",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_sub)
input_mul = Button(main_frame_bill,text="*",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_mul)
input_div = Button(main_frame_bill,text="/",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_div)

input_equal = Button(main_frame_bill,text="=",padx=29,pady=9,fg="black",background="lightblue",borderwidth=2,relief=RAISED,command= button_equal)
input_clear = Button(main_frame_bill,text="C",padx=29,pady=9,fg="black",background="violet",borderwidth=2,relief=RAISED,command= button_clear)

#Positioning buttons
input_1.grid(row=3,column=2)
input_2.grid(row=3,column=1)
input_3.grid(row=3,column=0)
input_4.grid(row=2,column=2)
input_5.grid(row=2,column=1)
input_6.grid(row=2,column=0)
input_7.grid(row=1,column=2)
input_8.grid(row=1,column=1)
input_9.grid(row=1,column=0)
input_0.grid(row=4,column=0)

input_add.grid(row=1,column=4)
input_sub.grid(row=2,column=4)
input_mul.grid(row=3,column=4)
input_div.grid(row=4,column=4)

input_equal.grid(row=4,column=2)
input_clear.grid(row=4,column=1)



#Creating a textbox for BILL
bill_generator = Text(main_frame_bill,height=15,width=30,borderwidth=5,relief=RAISED)
bill_generator.config(font=("Courier",13))
bill_generator.grid(row=5,rowspan=8,column=0,columnspan=10,pady=(15,10))


#Function to claculate and generate a bill
def total():
    cost_drink_input.delete(0, END)
    cost_food_input.delete(0, END)
    service_charge_input.delete(0, END)
    paid_tax_input.delete(0, END)
    sub_total_input.delete(0, END)
    total_cost_input.delete(0, END)

    global drink_amount
    global food_amount
    global bill_generator
    global sub_total
    global total_cost
    global drink_final_ar
    global food_final_ar
    global date1
    global time1

    drink_amount = 0
    food_amount = 0  

    drink_a = drinks_input_1.get()
    drink_b = drinks_input_2.get()
    drink_c = drinks_input_3.get()
    drink_d = drinks_input_4.get()
    drink_e = drinks_input_5.get()

    #All drink items
    drink_ar = [drink_a, drink_b, drink_c, drink_d, drink_e]

    for i in range(len(drink_ar)):
        if drink_ar[i] == '':
            drink_ar[i] = 0 
        else:
            drink_ar[i] = int(drink_ar[i])
        #Cost of drink items
        drink_amount += (drink_dict[i+1][1] * drink_ar[i])

    
    food_a = food_input_1.get()
    food_b = food_input_2.get()
    food_c = food_input_3.get()
    food_d = food_input_4.get()
    food_e = food_input_5.get()

    #All food items
    food_ar = [food_a, food_b, food_c, food_d, food_e]

    for i in range(len(food_ar)):
        if food_ar[i] == '':
            food_ar[i] = 0 
        else:
            food_ar[i] = int(food_ar[i])
        #Cost of food items
        food_amount += (food_dict[i+1][1] * food_ar[i])

    sc = (food_amount + drink_amount) * (5/100)
    sc = round(sc, 2)

    paid_tax = float((food_amount + drink_amount) * (6/100))
    paid_tax = round(paid_tax, 2)

    sub_total = sc + paid_tax
    sub_total = round(sub_total, 2)

    total_cost = drink_amount + food_amount + sc + paid_tax
    total_cost = round(total_cost, 2)

    date = datetime.date.today()
    date1 = str(date)
    t = time.localtime()
    
    time1 = str(t[3])+':'+str(t[4])+':'+str(t[5])

    drink_final_ar = []
    food_final_ar = [] 
    drink_cost = []
    food_cost = []
    drink = ''
    food = ''

    #for drinks
    #All Selected Drink items
    for i in range(len(drink_ar)):
        if drink_ar[i] > 0:
            drink_final_ar.append(drink_dict[i+1][0])
    
    #All Selected Drink items COST
    for i in range(len(drink_ar)):
        if drink_ar[i] > 0:
            drink_cost.append(drink_dict[i+1][1] * drink_ar[i])
    
    #Final DRINK Array
    for i in range(len(drink_cost)):
        drink += '\n   {}\t\t    {}'.format(drink_final_ar[i], drink_cost[i])
    
   
    #for food
    #All Selected Food items
    for i in range(len(food_ar)):
        if food_ar[i] > 0:
            food_final_ar.append(food_dict[i+1][0])
    
    #All Selected Food item COST
    for i in range(len(food_ar)):
        if food_ar[i] > 0:
            food_cost.append(food_dict[i+1][1] * food_ar[i])
    
    #Final FOOD Array
    for i in range(len(food_cost)):
        food += '\n   {}\t\t    {}'.format(food_final_ar[i], food_cost[i])
    

    bill_generator = Text(main_frame_bill,height=15,width=30,borderwidth=5,relief=RAISED)
    bill_generator.config(font=("Courier",13))
    bill_generator.grid(row=5,rowspan=8,column=0,columnspan=10,pady=(15,10))
    bill_generator.insert(1.0,"Bill no:xxx   Date:" + str(date) +"\n\t      time: " + time1 +"\n   ========================\n   Item(s)\t\t   Amount\n   ========================\n   " + drink + "\n   " + food + "\n\n   ----------------------\n   " + "Sub Total\t\t   "+ str(sub_total) + "\n   " + "Total\t\t   " + str(total_cost) )


    cost_drink_input.insert(0, drink_amount)
    cost_food_input.insert(0, food_amount)
    service_charge_input.insert(0, sc)
    paid_tax_input.insert(0 , paid_tax)
    sub_total_input.insert(0, sub_total)
    total_cost_input.insert(0, total_cost)



def mail():
    rcv = mail_input.get()
    bill = bill_generator.get('1.0', END)

    subject = "Bill Receipt"

    msg = f"Subject:{subject}\n\n{bill}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    #INSERT YOUR E-MAIL ID AND PASSWORD
    server.login("YOUR_e-mail", "YOUR_PASSWORD")
    server.sendmail("YOUR_e-mail", rcv, msg)

    server.quit()

    messagebox.showinfo("Message Sent", "Message Sent Successfully")



#SEND FUNCTION
def send():
    new = Tk()

    global bill_generator
    global mail_input

    main_label = Label(new, text="Send Bill",background="lightblue",fg="white",width=18,padx=5,pady=5)
    main_label.config(font=("Bold",32))
    main_label.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

    send_frame = LabelFrame(new, text="Send Bill Through SMS",borderwidth=3,padx=5,pady=5)
    send_frame.grid(row=2,column=0,columnspan=5,padx=10,pady=20)

    mail_label = Label(send_frame,text="Mail ID",relief=FLAT)
    mail_label.config(font=("Bold",15))
    mail_label.grid(row=1,column=0,padx=30,pady=(30,10))

    mail_input = Entry(send_frame,borderwidth=3,width=40)
    mail_input.grid(row=2,column=0,columnspan=5,padx=10,pady=(0,45))

    bill_label = Label(send_frame,text="Bill Details",relief=FLAT)
    bill_label.config(font=("Bold",16))
    bill_label.grid(row=3,column=0,columnspan=5,padx=20,pady=(30,15))

    drink_a = drinks_input_1.get()
    drink_b = drinks_input_2.get()
    drink_c = drinks_input_3.get()
    drink_d = drinks_input_4.get()
    drink_e = drinks_input_5.get()

    drink_ar = [drink_a, drink_b, drink_c, drink_d, drink_e]

    for i in range(len(drink_ar)):
        if drink_ar[i] == '':
            drink_ar[i] = 0 
        else:
            drink_ar[i] = int(drink_ar[i])

    
    food_a = food_input_1.get()
    food_b = food_input_2.get()
    food_c = food_input_3.get()
    food_d = food_input_4.get()
    food_e = food_input_5.get()

    food_ar = [food_a, food_b, food_c, food_d, food_e]

    for i in range(len(food_ar)):
        if food_ar[i] == '':
            food_ar[i] = 0 
        else:
            food_ar[i] = int(food_ar[i])

    date = datetime.date.today()
    t = time.localtime()

    drink_final_ar = []
    food_final_ar = []
    drink_cost = []
    food_cost = []
    drink = ''
    food = ''

    #For Drinks
    for i in range(len(drink_ar)):
        if drink_ar[i] > 0:
            drink_final_ar.append(drink_dict[i+1][0])
    
    for i in range(len(drink_ar)):
        if drink_ar[i] > 0:
            drink_cost.append(drink_dict[i+1][1] * drink_ar[i])

    for i in range(len(drink_cost)):
        drink += f'\n   {drink_final_ar[i]}\t\t    {drink_cost[i]}'
    
   
    #For Food
    for i in range(len(food_ar)):
        if food_ar[i] > 0:
            food_final_ar.append(food_dict[i+1][0])
    
    
    for i in range(len(food_ar)):
        if food_ar[i] > 0:
            food_cost.append(food_dict[i+1][1] * food_ar[i])
    

    for i in range(len(food_cost)):
        food += f'\n   {food_final_ar[i]}\t\t    {food_cost[i]}'

    #Generates bill in the Textbox
    bill_generator_2 = Text(send_frame,height=15,width=30,borderwidth=5,relief=RAISED)
    bill_generator_2.config(font=("Courier",13))
    bill_generator_2.grid(row=5,rowspan=8,column=0,columnspan=10,pady=(15,10))
    bill_generator_2.insert(1.0,"Bill no:xxx   Date:" + str(date) +"\n\t      time: " + str(t[3])+':'+str(t[4])+':'+str(t[5]) +"\n   ========================\n   Item(s)\t\t   Amount\n   ========================\n   " + drink + "\n   " + food + "\n\n   ----------------------\n   " + "Sub Total\t\t   "+ str(sub_total) + "\n   " + "Total\t\t   " + str(total_cost) )

    #Button to send an e-mail to the customer
    send_button_2 = Button(new,text="Send Bill",background="lightblue",fg="black",width=18,padx=5,pady=5, command=mail)
    send_button_2.grid(row=5,column=0,columnspan=5,padx=10,pady=30)

    new.quit()
 
    new.mainloop()


def reset():
    cost_drink_input.delete(0, END)
    cost_food_input.delete(0, END)
    service_charge_input.delete(0, END)
    paid_tax_input.delete(0, END)
    sub_total_input.delete(0, END)
    total_cost_input.delete(0, END)

    drinks_input_1.delete(0, END)
    drinks_input_2.delete(0, END)
    drinks_input_3.delete(0, END)
    drinks_input_4.delete(0, END)
    drinks_input_5.delete(0, END)

    food_input_1.delete(0, END)
    food_input_2.delete(0, END)
    food_input_3.delete(0, END)
    food_input_4.delete(0, END)
    food_input_5.delete(0, END)

    bill_generator.delete(1.0, END)



#BUTTONS
total_button = Button(main_frame_option,text="Total",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED, command=total)
save_button = Button(main_frame_option,text="Save",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED)
send_button = Button(main_frame_option,text="Send",padx=31,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED, command=send)
exit_button = Button(main_frame_option,text="Exit",padx=33,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED)
update_button = Button(main_frame_option,text="Update",padx=23,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED)
reset_button = Button(main_frame_option,text="Reset",padx=29,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED, command=reset)


total_button.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
save_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
send_button.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
exit_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
update_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
reset_button.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

root.mainloop()