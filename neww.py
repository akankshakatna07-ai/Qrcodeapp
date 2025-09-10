import streamlit as s 
import qrcode

url_input = s.text_input("Enter URL : ")
image_name = s.text_input("Enter file name : ")

if s.button("submit"):
    gen_qr = qrcode.make(url_input)
    img_save = gen_qr.save(f"{image_name}.png")
    s.image(f"{image_name}.png")