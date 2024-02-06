from user import User

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        print("privileges")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])
