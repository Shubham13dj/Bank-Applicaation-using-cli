import transaction
import time
def main():
       print("\n========================================================")
       print("*******************Welcome to Chatrapati bank******************")
       print("========================================================")
       print("1 : Deposit Ammount ")
       print("2 : Withdraw Ammount ")
       print("3 : Balance Enquiry ")
       print("4 : Display Coustomer Details ")
       print("5 : Display Transaction History")
       print("6 : Exit ")
       print("---------------------------------------------------------")
       m=int(input("Enter your choice:"))
       if(m==1):
            print("\n=========================================================")
            print("|                  Deposit Money in your account        | "   )
            print("---------------------------------------------------------\n")
            amt=int(input("Enter Amount to Deposit : "))
            dat = time.ctime()
            transaction.depo(amt,dat)
            transaction.balance+=amt
            print("Amount Credited Successfully!!")
            time.sleep(3)
            main()
       elif(m==2):
            print("\n=========================================================")
            print("|              Withdraw Money from your account         |")
            print("---------------------------------------------------------\n")
            amt=int(input("Enter Amount to Withdraw : "))
            dat = time.ctime()
            transaction.withd(amt,dat)
            transaction.balance-=amt 
            print("Amount Debited Successfully!!")
            time.sleep(3)
            main()
       elif(m==3):
            print("\n=========================================================")
            print("|                Check Balance in your account          |")
            print("---------------------------------------------------------\n")
            print("Your current balance is Rs:  {:0.3f}".format(transaction.balance))
            time.sleep(3)
            main()
       elif(m==4):
            transaction.cus_details()
            time.sleep(3)
            main()
       elif(m==5):
           transaction.trans()
           time.sleep(3)
           main()
       elif(m==6):
            print("!!Thanks For Using our Software!!")
            exit(0)
       else:
           print("Please Enter Valid Option!!!")
           time.sleep(2)
           main()
def login():
    print("\n========================================================")
    print("******************Login to your account*****************")
    print("========================================================\n")
    user_name=input("Enter your User name:")
    global user_pass
    user_pass=input("Enter your Password:")
    if(user_pass == transaction.u_pass and user_name==transaction.u_name):
        time.sleep(2)
        main()
    else:
        print("Please enter correct User name and Password")
        time.sleep(2)
        login()
def new_acc():
    transaction.new_acc()
def log():
    print("\n========================================================")
    print("************Welcome to Chatrapati bank of India**********")
    print("========================================================")
    print("1 : Login to your account ")
    print("2 : Open New account ")
    print("3 : Exit \n")
    print("-----------------------------------------------------------\n")
    c=int(input("Enter your choice:"))
    if(c==1):
        login()
    elif(c==2):
        new_acc()
        print("Account Created Successfully!!!") 
        time.sleep(2)
        log()
    elif(c==3):
       print("!!Thanks For Using our Software, Visit again!!")
       exit(0)
    else:
           print("Please Enter Valid Option!!!")
           log()
log()