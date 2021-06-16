import time
depo_list=[]
time_list=[]
time1_list=[]
with_list=[]
def depo(amt,dat):
    depo_list.append(amt)
    time_list.append(dat)
def withd(amt,dat):
    with_list.append(amt)
    time1_list.append(dat)
def trans():
    print("\n========================================================")
    print("*******************Transaction History******************")
    print("========================================================\n")
    j=0
    n=0
    print("Deposited Amount\t\t\t Duration")
    print("---------------------------------------------------------\n")
    for i in depo_list:
        print("\t{:0.3f}".format(depo_list[j]),end="\t\t\t")
        for m in time_list:
            print(time_list[n])
            break
        j+=1
        n+=1
    print("\n Withdrawl Amount\t\t\t Duration")
    print("---------------------------------------------------------\n")
    f=0
    t=0
    for k in with_list:
       print("\t{:0.3f}".format(with_list[f]),end="\t\t\t")
       for y in time1_list:
            print(time1_list[t])
            break
       t+=1
       f+=1    
def new_acc():
    global u_pass,c_pass,balance,name,email,phone_no,act_type,address,u_name
    print("\n========================================================")
    print("********************Create Your account********************")
    print("========================================================\n")
    name=input("Enter your full name:")
    email=input("Enter your E-mail:")
    phone_no=input("Enter your Mobile Number:")
    gender=input("Enter your Gender:")
    dob=input("Enter your Birth date:")
    address=input("Enter your Address:")
    u_name=input("Create user name for login:")
    u_pass=input("Create password:")
    c_pass=input("Confirm your password:")
    if(u_pass==c_pass):
        pass
    else:
        print("Password does not match!!!")
        c_pass=input("Confirm your password:")
    print("1: Saving\n2: Current")
    act_type=int(input("Select Account Type:"))
    if(act_type==1):
        print("If you deposit more than 500Rs then only you will able to open new saving account")
        balance=int(input("Enter amount to open account:"))
        if(balance<500):
            print("Minimum deposit amount is 500")
            balance=int(input("Enter amount to open account:"))
            amt=balance
            dat = time.ctime()
            depo(amt,dat)
    elif(act_type==2):
        print("If you deposit more than 1000Rs then only you will able to open new current account")
        balance=int(input("Enter amount to open account:"))
        if(balance<1000):
            print("Minimum deposit amount is 1000")
            balance=int(input("Enter amount to open account:"))
            dat = time.ctime()
            depo(balance,dat)
def cus_details():
    print("\n========================================================")
    print("********************CUSTOMER DETAILS********************")
    print("========================================================\n")
    print("customer Name: ",name)
    print("Customer E-mail: ",email)
    print("Customer Mobile no.: ",phone_no)
    print("Customer Address: ",address)

    