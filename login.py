class login:
    def auth(self):
        while True:
            user_name=input('Enter Your User Name: ')
            password=input('Enter Your Password: ')
            if user_name==password:
                print('Login Successful')
                break
            else:
                print('Enter valid credentials')
obj=login()
obj.auth()
            
