class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class LoginSystem:
    def __init__(self):
        self.users = {}
        self.max_attempts = 3

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Choose another username.")
        else:
            user = User(username, password)
            self.users[username] = user
            print("User registered successfully.")

    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                print("Login successful!")
            else:
                print("Incorrect password. Please try again.")
                self.retry_login(username, password)
        else:
            print("User not found. Please register.")

    def retry_login(self, username, correct_password):
        attempts = 1
        while attempts < self.max_attempts:
            password = input("Enter the correct password: ")
            if password == correct_password:
                print("Login successful!")
                break
            else:
                print("Incorrect password. Please try again.")
                attempts += 1
        else:
            print("Maximum login attempts reached. Account locked.")

login_system = LoginSystem()

login_system.register_user("user1", "password123")

login_system.login("user1", "wrongpassword")

login_system.retry_login("user1", "password123")
