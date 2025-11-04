import streamlit as st
import requests

# ---------------- Page Config ----------------
st.set_page_config(page_title="Quran App", layout="wide")

# ---------------- Custom CSS Styling ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        background-color: #0e1117;
        color: #ffffff;
    }

    .main {
        background-color: #0e1117;
        padding: 2rem;
        border-radius: 15px;
    }

    .title {
        font-family: 'Amiri', serif;
        text-align: center;
        font-size: 48px;
        color: #00d4a1;
        margin-bottom: 10px;
    }

    .sub-title {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        color: #cccccc;
        margin-bottom: 40px;
    }

    .surah-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        transition: 0.3s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }

    .surah-box:hover {
        transform: scale(1.02);
        background: rgba(0, 212, 161, 0.08);
        border-color: #00d4a1;
    }

    .arabic-text {
        font-family: 'Amiri', serif;
        font-size: 28px;
        direction: rtl;
        text-align: right;
        color: #ffffff;
        line-height: 2;
        margin-bottom: 10px;
    }

    .ayah-number {
        color: #00d4a1;
        font-size: 20px;
        text-align: right;
        margin-bottom: 8px;
        font-family: 'Poppins', sans-serif;
    }

    audio {
        width: 100%;
        margin-top: 8px;
        outline: none;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown("<h1 class='title'>📖 Quran App</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Listen and read Quran with beautiful Arabic font</p>", unsafe_allow_html=True)

# ---------------- Fetch Surah List ----------------
surah_list = requests.get("http://api.alquran.cloud/v1/surah").json()["data"]
surah_name = [f"{s['number']} . {s['englishName']} ({s['name']})" for s in surah_list]

# ---------------- Surah Selection ----------------
select_surah_name = st.selectbox("Choose Surah", surah_name)
surah_num = int(select_surah_name.split(" . ")[0])

# ---------------- Fetch Surah Ayahs ----------------
surah_list_ayahs = requests.get(
    f"http://api.alquran.cloud/v1/surah/{surah_num}/ar.alafasy"
).json()["data"]["ayahs"]

# ---------------- Display Ayahs ----------------
for ayah in surah_list_ayahs:
    st.markdown(f"""
        <div class='surah-box'>
            <div class='ayah-number'>Ayah {ayah['numberInSurah']}</div>
            <p class='arabic-text'>{ayah['text']}</p>
        </div>
    """, unsafe_allow_html=True)
    st.audio(ayah["audio"])
