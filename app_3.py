#streamlit 연습

import streamlit as st

st.title("streamlit 연습")
st.info("파란색 알림 박스입니다.")
st.success("초록색 성공 메시지입니다.")

col1, col2 = st.columns(2)

#데이터 입력 연습

name = st.text_input("이름")
btn = st.button("로그인")

#폼 입력 & 상태 관리 연습

with st.form("my_form"):
    submit = st.form_submit_button("전송")

st.session_state.login = True
