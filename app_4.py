#streamlit 페이지 편집 연습

import streamlit as st

#제목 설정
st.title("🐰전해인의 첫 streamlit 웹 앱🤩")


#텍스트 출력
st.info("파이썬, Streamlit으로 제작한 웹 애플리케이션입니다.")


#사용자 입력 받기

# name = st.text_input("이름을 입력해 주세요.")

if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름을 입력해 주세요")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)


#columns 설정
st.subheader("웹 제작 정보")

col1, col2 = st.columns(2)
with col1:
    st.write("● 제작 날짜: 2026. 10. 27.")
    st.write("● 제작 요일: 수요일")
with col2:
    st.write("● 제작 시간: 11:30 ~ 12:40")
    st.write("● 제작 장소: 그린컴퓨터아트학원")



#버튼 클릭 이벤트
if st.button("인사하기"):
    if name:
        st.success(f"안녕하세요, {name}님!🙌")
    else:
        st.warning("이름을 입력해 주세요.")


#리스트 출력
task = "0"
tasks = [
    "1. streamlit 활용하여 웹 페이지 만들기 "
    "2. streamlit 제공 메서드 공부하기 "
    "3. 지난 시간에 배운 파이썬 내용 복습하기 "
]

st.subheader("✅ 금일 할 일 목록 ✅")

for task in tasks:
    #border=True를 주면 각 반복 요소가 단정한 상자로 감싸짐
    with st.container(border=True):
        st.write(task)
