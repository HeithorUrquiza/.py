class UserRegister:
    
    def add_user(self):
        print("Welcome to Prisma Flight Club.")
        print("We find the best flight deals and email you.")
        f_name = input("What is your first name?\n")
        l_name = input("What is your last name?\n")
        email1 = "email1"
        email2 = "email2"
        
        while email1 != email2:
            email1 = input("What is your email?\n").lower()
            if email1 == "quit" or email1 == "exit":
                exit()
        
            email2 = input("Type your email again.\n").lower()
            if email2 == "quit" or email2 == "exit":
                exit()
        print("Nice! You're in the club now")        
        return (f_name, l_name, email1)