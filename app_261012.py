import streamlit as st

st.title("✅나의 일정관리 앱")
st.info("이름과 일정을 입력하고 출력하는 페이지입니다.")

st.subheader("이름을 입력하세요.")
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text.input("")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)

