s_username="EMC"
s_password="123"

uname=input("enter your username:")
password=input("enter  your password:")

def validate():
    if(s_username==uname and s_password==password):
        print("correct")
    else:
        print("wrong")
validate()

s_username="EMC"
s_password="123"

uname=input("enter your username:")
password=input("enter  your password:")

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)

