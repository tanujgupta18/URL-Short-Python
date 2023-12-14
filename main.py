import streamlit as st
import pyshorteners

def short_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

st.title("URL Shortener App")

url = st.text_input("Enter the URL:")
if st.button("Shorten URL"):
    if url:
        short_url_result = short_url(url)
        st.success(f"Shortened URL: {short_url_result}")
    else:
        st.warning("Please enter a URL")
