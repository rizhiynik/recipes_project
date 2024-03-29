import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

# --- SETTING CONFIGURATION ---
st.set_page_config(page_title="Recipes Project")

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "recipes_project",  # For a reason, doesn't return to login page
    "adcdef",
    cookie_expiry_days=30,
)

name, authenticaton_status, username = authenticator.login("Login", "main")

if authenticaton_status is False:
    st.error("Username/password is incorrect")

if authenticaton_status is None:
    st.warning("Please enter your username and password")

if authenticaton_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
