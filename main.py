import streamlit as st

import requests

st.set_page_config(page_title="Quran App")

st.title("Quran App")

surah_list = requests.get("http://api.alquran.cloud/v1/surah").json()["data"]

surah_name = [f"{s["number"]} . {s["englishName"]} {s["name"]}"  for s in surah_list]

select_surah_name=st.selectbox("Choose Surah" , surah_name)

surah_num= int(select_surah_name.split(" . ")[0])


surah_list_ayahs = requests.get(f"http://api.alquran.cloud/v1/surah/{surah_num}/ar.alafasy").json()["data"]["ayahs"]

for ayah in surah_list_ayahs:
    st.write(ayah["text"])
    st.audio(ayah["audio"])



