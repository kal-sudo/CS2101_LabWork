import re
def check_pass():
        while True:
            password=str(input("Enter the password:"))
            f1=re.search(r"\d",password) 
            f2=re.search(r"[a-z]",password) 
            f3=re.search(r"[A-Z]",password) 
            f4=not re.search(r"\s",password)
            f5=re.search(r"[^a-zA-Z0-9]",password)
            if( 
            f1 and f2 and f3 and f4 and f5
            ):
                 print("Valid Password")
                 break
            else:
                if(not f1):
                 print("Invalid Password, no digits")
                 continue
                elif(not f2):
                 print("Invalid Password, no small letters")
                 continue   
                elif(not f3):
                    print("Invalid Password, no capital letters")
                    continue
                elif(not f4):
                    print("Invalid Password, whitespace character")
                    continue
                elif(not f5):
                    print("Invalid Password, no special chars")
                    continue
                else:
                    print("Length of password is less than 8")

        return() 

check_pass()