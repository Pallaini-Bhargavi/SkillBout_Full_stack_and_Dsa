class User:
    def login(self):
        print("Login")

class BusinessUser:
    def runadd(self):
        u = User()
        u.login()
        print("Run add")

b = BusinessUser()

b.runadd()