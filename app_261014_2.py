#firebase 활용 로그인 / 로그아웃 웹 제작

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

#웹 코딩 부분
#로그인 세션 및 회원가입 로직

if "login" not in st.session_state: st.session_state["login"] = False

if st.session_state["login"]:
    st.title("나의 다이어리 웹✒️")
    if st.button("로그아웃"): st.session_state["login"] = False; st.rerun()

    with st.form("input_form", clear_on_submit=True):
        d_day = st.text_input("날짜를 적으세요.")
        d_task = st.text_input("할 일을 적으세요.")
        sub = st.form_submit_button("추가")
    
    if sub and task2:
        db.collection("diary").add({"d_date": d_day, "d_content": d_task, "at": firestore.SERVER_TIMESTAMP})
        st.success(f"'{d_task}' 추가됨!")

    docs = db.collection("diary").stream()
    for doc in docs:
        st.info(doc.to_dict()["d_date"])
        st.write(doc.to_dict()["d_content"])
        if st.button("삭제", key=doc.id):
            db.collection("todos").document(doc.id).delete()
            st.rerun()


else:

    tab1, tab2 = st.tabs(["로그인", "회원가입"])
    with tab1:
        l_id_key = st.text_input("아이디", key="l_id_key")
        l_pw_key = st.text_input("비번", type="password", key="l_pw_key")
        if st.button("로그인"):
            u = db.collection("users").document(l_id_key).get()
            if u.exists and u.to_dict()["password"] == l_pw_key:
                st.session_state["login"] = True; st.rerun()

    with tab2:
        n_id_key = st.text_input("새 아이디", key="n_id_key")
        n_pw_key = st.text_input("새 비번", type="password", key="n_pw_key")
        if st.button("가입하기"):
            db.collection("users").document(n_id_key).set({"password": n_pw_key})
            st.success("회원가입 완료!")
