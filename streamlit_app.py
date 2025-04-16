import streamlit as st

st.title("Ürün Sayım Uygulaması")

urun_listesi = []

urun_sayisi = st.number_input("Kaç farklı ürün sayacaksınız?", min_value=1, step=1)

for i in range(int(urun_sayisi)):
    st.subheader(f"Ürün {i+1}")
    urun_adi = st.text_input(f"Ürün adı {i+1}", key=f"ad_{i}")
    adet = st.number_input(f"{urun_adi} için adet giriniz", min_value=0, key=f"adet_{i}")
    urun_listesi.append((urun_adi, adet))

if st.button("Sonuçları Göster"):
    st.subheader("Sayım Sonuçları")
    for urun, adet in urun_listesi:
        if urun:
            st.write(f"{urun}: {adet} adet")
