class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""\nWelcome to Chatbook!! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           \nYour choice: """)    

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.message_friend()
        else:
            print("Exiting... Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Set up your password here -> ")
        self.username = email
        self.password = pwd
        print("✅ You have signed up successfully!!\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu.")
        else:
            email  = input("Enter your email -> ")  
            pwd = input("Enter your password -> ") 
            if email == self.username and pwd == self.password:
                self.loggedin = True
                print("You are now logged in!")
            else:
                print("Invalie credentials!")    
        self.menu()

    def write_post(self):
        if self.loggedin == True:
            post = input("Write your post here -> ")
            print(f"📝 Post saved: {post}\n")
        else:
            print("❌ You must sign in first!\n")
        self.menu()

    def message_friend(self):
        if self.loggedin == True:
            friend = input("Enter your friend’s name -> ")
            msg = input(f"Write your message to {friend} -> ")
            print(f"📩 Message sent to {friend}: {msg}\n")
        else:
            print("❌ You must sign in first!\n")
        self.menu()


# Run program
obj = Chatbook()



