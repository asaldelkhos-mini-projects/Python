# a little advanced one
# Warning:  this is not a secure way, it's just for fun & practice

pwd = input("What is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {passw}")

def add():
    name = input("Account name: ")
    pws = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd +  "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), or press 'q' to quit? ")
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue
