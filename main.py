import streamlit as st
import requests

# ---------------- Config ----------------
st.set_page_config(page_title="Quran App")

# ---------------- Custom Arabic Font ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');

    .arabic-text {
        font-family: 'Amiri', serif;
        font-size: 28px;
        direction: rtl;
        text-align: right;
        line-height: 2;
    }
    .title {
        font-family: 'Amiri', serif;
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown("<h1 class='title'>📖 Quran App</h1>", unsafe_allow_html=True)

# ---------------- Surah List ----------------
surah_list = requests.get("http://api.alquran.cloud/v1/surah").json()["data"]

surah_name = [f"{s['number']} . {s['englishName']} {s['name']}" for s in surah_list]

select_surah_name = st.selectbox("Choose Surah", surah_name)
surah_num = int(select_surah_name.split(" . ")[0])

# ---------------- Fetch Surah Ayahs ----------------
surah_list_ayahs = requests.get(
    f"http://api.alquran.cloud/v1/surah/{surah_num}/ar.alafasy"
).json()["data"]["ayahs"]

# ---------------- Display Ayahs ----------------
for ayah in surah_list_ayahs:
    st.markdown(f"<p class='arabic-text'>{ayah['text']}</p>", unsafe_allow_html=True)
    st.audio(ayah["audio"])
