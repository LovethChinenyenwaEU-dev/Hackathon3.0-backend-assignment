# admin.py
from user import User

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can delete post", "can ban user", "can add post"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
