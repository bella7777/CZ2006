import streamlit as st
from User import User
from hashlib import sha256

class LoginDisplay:
    def __init__(self,user):
        self.user = user # temporary
        self.submit = False

    # temporary for testing
    # @staticmethod
    def getUser(self,username):
        return self.user

    # consider using firebase to handle data
    # @staticmethod
    # def getUser(username):
    #     return self.user

    @staticmethod
    def login(user,passwordHash):
        if user.verifyPassword(passwordHash):
            return user
        else:
            return False

    def renderDisplay(self):
        st.markdown('# LOGIN')
        username = st.text_input("Username")
        password = st.text_input("Password",type = 'password')
        passwordHash = sha256(password.encode('utf-8')).hexdigest()
        if st.button('Submit'):
            user = self.getUser(username)
            if self.login(user,passwordHash):
                loggedIn = True
                resultUser = user
            else:
                loggedIn = False
                resultUser = None
                st.write('## Login failed')
        else:
            return False,None
        return loggedIn,resultUser
        
if __name__ == "__main__":
    user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'',1,1)
    f = LoginDisplay(user).renderDisplay()
    print(f)