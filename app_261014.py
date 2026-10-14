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


st.title("✅TODO 리스트")

#with st.form("input_form", clear_on_submit=True):
#    date = st.text_input("날짜를 적으세요.")
#    sub = st.form_submit_button("추가")

#if sub and task:
#    db.collection("date").add({"content": date, "at": firestore.SERVER_TIMESTAMP})
#    st.success(f"'{date}' 추가됨!")

#입력값 받기
with st.form("input_form", clear_on_submit=True):
    day = st.text_input("날짜를 적으세요.")
    task = st.text_input("할 일을 적으세요.")
    sub = st.form_submit_button("추가")
    
if sub and task:
    db.collection("todos").add({"date": day, "content": task, "at": firestore.SERVER_TIMESTAMP})
    st.success(f"'{task}' 추가됨!")


st.subheader("Todo 리스트 출력")

docs = db.collection("todos").stream()

for doc in docs:
    col1, col2, col3 = st.columns([8, 3])
    col1.info(doc.to_dict()["date"])
    col2.info(doc.to_dict()["content"])
    if col3.button("삭제", key=doc.id):
        db.collection("todos").document(doc.id).delete()
        st.rerun()
