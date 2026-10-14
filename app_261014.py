#firebase 활용 웹 제작

import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore



st.title("해인이의 메모장")

with st.form("input_form", clear_on_submit=True):
    task = st.text_input("텍스트를 적으세요.")
    sub = st.form_submit_button("추가")

if sub and task:
    db.collection("todos").add({"content": task, "at": firestore.SERVER_TIMESTAMP})
    st.success(f"'{task}' 추가됨!")
