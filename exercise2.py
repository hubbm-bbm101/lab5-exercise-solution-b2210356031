valid = False
while valid == False:
    email = input("Enter your email: ")
    if "@" in email:
        if "." in email:
            valid = True
            print("It is a valid email. Thank you")
        else:
            print("Please write a valid email. Try again")
            valid = False
    else:
        print("Please write a valid email. Try again")
        valid = False


