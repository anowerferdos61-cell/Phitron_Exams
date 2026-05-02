class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
 
    def login(self,username,password):
        if self.username == username and self.password == password:
            return True
        return False