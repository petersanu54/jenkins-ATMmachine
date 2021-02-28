import time

pin = 1234




#############################################################################

def main_screen():
    
    print("\nWelcome to 24x7 Bharat Bank ATM")

    key = str(input("\nEnter y to continue "))
    second_screen(key)

#############################################################################
def second_screen(key):

    if key == 'y' or key == 'Y':
        print('\nInsert your ATM/Debit/Shoppping card')
        time.sleep(2)
        tries = 1
        

        while True:
            tempPin = int(input("\nEnter your 4 digit secret pin "))
            if tempPin == pin and tries <=3:
                start_session()                

            else:
                print("\nwrong ping entered")
                if tries >= 3:
                    print("\nMaximum limits crossed!...Exiting. Thanks for visiting!!")
                    main_screen()
                    
                else:
                    tries +=1
                    continue
            
    else :
        print("\nExiting. Thanks for visiting!!")
        main_screen()


####################################################################################

def start_session():
            print('\nHello User. Welcome to Bharat Bank 24x7 ATM. Please see the below facilites ')
            balance = 25000
            while True:
                
                try:
                    print('''\n
                        1. Balance check
                        2. Withdrawl
                        3. Deposit
                        4. exit
                    ''')
                    option = int(input('\nPlease enter the option number '))

                    if option == 1:
                        time.sleep(2)
                        print(f"\nMain account balance : {balance}")
                        print("\n*****************************************************************")
                        print("\n*****************************************************************")
                        continue
                    
                    elif option == 2:
                        amount  = int(input("\n Enter the withdrawl amount "))
                        balance -= amount
                        time.sleep(1)
                        print("\nprocessing.....")
                        time.sleep(3)
                        print("\nWithdrawl complete. Please collect your cash from the dispenser ")
                        print(f"\nCurrent balance - {balance}")
                        print("\n*****************************************************************")
                        print("\n*****************************************************************")
                        time.sleep(2)
                        continue

                    elif option == 3:
                        deposit = int(input("Enter the deposit amount  "))
                        time.sleep(1)
                        print("\nOpening the deposit drawer")
                        time.sleep(2)
                        print("\nPlace cash in the deposit drawer")
                        print("\nprocessing.......")
                        time.sleep(2)
                        balance += deposit
                        print(f'\nAvailable balance : {balance}')
                        print("\n*****************************************************************")
                        print("\n*****************************************************************")
                        time.sleep(2)
                        continue

                    elif option == 4:
                        print("\n*****************************************************************")
                        print("\n*****************************************************************")
                        print("\nExiting. Thanks for visiting!!")
                        main_screen()

                    else:
                        print('\nenter a valid option')
                        print("\n*****************************************************************")
                        print("\n*****************************************************************")


                except:
                    print('\nenter a valid option')
                    print("\n*****************************************************************")
                    print("\n*****************************************************************")



##########################################################################

#############################################################################

main_screen()
