import streamlit as st

st.title("✅나의 일정관리 앱")
st.info("이름과 일정을 입력하고 정보를 출력하는 페이지입니다.")


st.subheader("정보 입력 부분입니다.")
if "user_list" not in st.session_state:
    st.session_state.user_list = []


with st.form("input_form1"):
    name = st.text_input("이름을 입력하세요.")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)


with st.form("input_form2"):
    name = st.text_input("일정을 입력하세요.")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(schedule)

col1, col2 = st.columns(2)

task = "0"
tasks = [
    "① streamlit 웹 설계하기",
    "② streamlit 웹 배포하기",
    "③ 오류 있는지 확인하기"
]

if st.button("입력한 내 일정 보기👀"):
    with col1:
        st.success(f"안녕하세요, {name}님!")
        st.subheader("일정 안내")
        st.write(schedule)

    with col2:
        st.write("기존 일정입니다.")
        for task in tasks:
            with st.container(border=True):
                st.write(task)



