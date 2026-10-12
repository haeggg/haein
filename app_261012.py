import streamlit as st

st.title("✅나의 일정관리 웹")
st.info("이름과 일정을 입력하고 정보를 출력하는 페이지입니다.")


st.subheader("─ 정보 입력 부분입니다. ──────────────")
if "user_list" not in st.session_state:
    st.session_state.user_list = []

col1, col2, col3 = st.culumns(3)

with col1:

    with st.form("input_form1"):
        name = st.text_input("1. 이름을 입력하세요.")
        if st.form_submit_button("등록") and name:
           st.session_state.user_list.append(name)

with col2:

    with st.form("input_form2"):
        date = st.text_input("2. 날짜를 입력하세요.")
        if st.form_submit_button("등록") and name:
            st.session_state.user_list.append(date)
with col3:
    
    with st.form("input_form3"):
        schedule = st.text_input("3. 일정을 입력하세요.")
        if st.form_submit_button("등록") and name:
            st.session_state.user_list.append(schedule)

col4 = st.columns(1)

with col4:
    st.subheader("─ 입력한 내 일정 보기👀 ─────────────")
    if st.button("버튼을 눌러 확인하기"):

        st.success(f"안녕하세요, {name}님!")
        st.subheader("일정 안내")

        col1, col2 = st.columns(2)
        task = "0"
        tasks = [
            "① streamlit 웹 설계하기",
            "② streamlit 웹 배포하기",
            "③ 오류 있는지 확인하기"
        ]

        with col1:
            st.info(f"{date} / 입력한 일정입니다.")
            with st.container(border=True):
                st.write(f"① {schedule}")

        with col2:
            st.info("기존 일정입니다.")
            for task in tasks:
                with st.container(border=True):
                    st.write(task)



