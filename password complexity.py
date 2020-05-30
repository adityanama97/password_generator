#regular expression to say the password is strong.
#((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{6,20})

# regular expression to tell the password is weak.
#((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{6,20})

import re
v=input("Enter the password:")
if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")
else:
    print("You have entered an invalid password.")
    
