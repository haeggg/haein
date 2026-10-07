#streamlit 페이지 편집 연습

import streamlit as st

st.title("전해인의 첫 웹🤩")
st.info("파이썬만으로 제작하는 UI입니다.")

col1, col2 = st.columns(2)
with col1:
    st.success("제작 날짜: 2026. 10. 27.")
with col2:
    st.write("제작 요일: 수요일")

# 새로고침 시 데이터 유지

if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)
