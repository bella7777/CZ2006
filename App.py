import streamlit as st
from SearchDisplay import SearchDisplay
from LoginDisplay import LoginDisplay
from User import User
from hashlib import sha256
import SessionState
from IndividualDisplay import IndividualDisplay
from st_rerun import rerun
from streamlit.ScriptRunner import StopException, RerunException
from streamlit.ScriptRequestQueue import RerunData

def App():
    session_state = SessionState.get(loggedIn = False,selectedOption = "Home",user = None)

    user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'',1,1)
    
    if session_state.loggedIn:
        # print("here")
        st.sidebar.markdown("Welcome, {}!".format(session_state.user.getUserName()))
        profileButton = st.sidebar.button("Profile")
        if profileButton:
            session_state.selectedOption = "Profile"
    else:
        loginButton = st.sidebar.button("Login")
        if loginButton:
            session_state.selectedOption = "Login"
            user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'',1,1)

    homeButton = st.sidebar.button("Home")
    if homeButton:
        session_state.selectedOption = "Home"

    if session_state.selectedOption == "Login":
        loggedIn,user = LoginDisplay(user).renderDisplay()
        if loggedIn:
            session_state.loggedIn = loggedIn
            session_state.user = user
            session_state.selectedOption = "Profile"
            rerun()

    elif session_state.selectedOption == "Home":
        SearchDisplay().renderDisplay()

    elif session_state.selectedOption == "Profile":
        IndividualDisplay(session_state.user).renderDisplay()
App()