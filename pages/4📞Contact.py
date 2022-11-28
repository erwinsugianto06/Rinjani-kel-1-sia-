import streamlit as st


col1, col2, col3 = st.columns(3)
with col1:
    st.header("Kontak Kami")
    st.write(" Anda bisa menghubungi kami melalui berbagai kontak sosial media kami. Jangan ragu untuk menghubungi kami. ")
    
with col2:
    st.write(" ")
with col3:
    st.header("Masukkan")
    st.write(" Kami sangat terbuka untuk menerima kritik dan saran. Kami berharap masukan dari anda bisa menjadi perubahan yang baik.")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("kontak-removebg-preview.png")

with col2:
    st.write(" ")

with col3:
    st.text_input("Masukkan Nama")
    st.text_input("Masukkan Email")
    st.text_input("Masukkan No.Hp")
    st.text_area("Pesan anda")
    button_clicked= st.button("Selesai")
    

    


  


