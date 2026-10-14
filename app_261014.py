#firebase 활용 웹 제작

import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore


#firebase 중복 초기화 방지

if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()


st.title("해인이의 메모장")

with st.form("input_form", clear_on_submit=True):
    task = st.text_input("텍스트를 적으세요.")
    sub = st.form_submit_button("추가")

if sub and task:
    db.collection("todos").add({"content": task, "at": firestore.SERVER_TIMESTAMP})
    st.success(f"'{task}' 추가됨!")
