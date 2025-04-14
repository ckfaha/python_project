from cryptography.fernet import Fernet


'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb")as file_key:
        file_key.write(key)
write_key()'''

def load_key():
    file=open("key.key",'rb')
    keys=file.read()
    file.close()
    return keys

key=load_key()
fer=Fernet(key)

def create():
    usern=input("Enter Username:")
    password=input("Enter password :")

    with open('password.txt','a')as f:
        f.write(usern+"|"+fer.encrypt(password.encode()).decode()+'\n')

def view():
    with open('password.txt','r')as f:
        for line in f.readlines():
            data=line.rstrip()
            user,password=data.split("|")
            print("User:",user,"| Password:",fer.decrypt(password.encode()).decode())
            

while True:
    passw=input("Would you like to create an acoount or view the existing one or (q) to quit this '(view/create)': ").lower()
    if passw == "q":
        break

    if passw=="create":
        create()

    elif passw=="view":
        view()

    else:
        print("Invalid Mode")
        continue