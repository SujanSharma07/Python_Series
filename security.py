import random
import string

m_strength = ["medium", "MEDIUM","Medium"]
s_strength = ["STRONG", "strong","Strong"]


def passGen(strength, passLength=8):
    try:
        if passLength <= 12 and passLength >= 8:
            if strength in m_strength:
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(passLength))
            elif strength in s_strength:
                letters = string.ascii_letters + "1234567890!@#$%^&*()_+?}<{"
                return ''.join(random.choice(letters) for i in range(passLength))
	  
        else:
            raise Exception

    except:
        print(f"Password Length must be between 8-12, You Entered {passLength} Characters only")

while(True):
	type_ = input(" Enter the strength of password you want i.e either strong or medium: ")

	length = int( input("Enter the length of to be generated PASSWORD: " ) )
	password = passGen(type_, length)
	print(f"Generated Password of length {length} and strength {type_} is:  ",password)
	print("\n\n***********************\n\n")
