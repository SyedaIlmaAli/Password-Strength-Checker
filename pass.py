import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon= "🔒")
st.title("🔒 Password Strength Checker")

st.markdown("""
### Welcome to the ultimate password strength checker! 👋
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            We will give you helpful tips to create a **Strong Password** 🔒
""")

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be atleast 8 characters long.")
    if re.search(r'[A-Z]', password) and (r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain atleast 1 digit.")
    if re.search(r'[!@#$%&]', password):
        score += 1
    else:
        feedback.append("❌Password should contain atleast 1 special character(!@#$%&).")
    if score == 4:
        feedback.append("✅Your password is strong! 🎉")
    elif score == 3:
        feedback.append("🟡Your password is medium. It could be stronger.")
    else:
        feedback.append("🔴Your password is week. Make it stronger.")
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")