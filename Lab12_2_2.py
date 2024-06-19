import streamlit as st
import time
import webbrowser

st.title("Xác thực đăng nhập")

correct_username = "21522747"
correct_password = "10072003"

username = st.text_input("Tên đăng nhập")
password = st.text_input("Mật khẩu", type="password")

if st.button("Đăng nhập"):
    if username == correct_username and password == correct_password:
        st.success("Đăng nhập thành công")
        time.sleep(3)  
        webbrowser.open("https://www.uit.edu.vn")
    else:
        st.error("Tên đăng nhập hoặc mật khẩu không đúng")
