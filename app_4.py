#streamlit 페이지 편집 연습

import streamlit as st

#제목 설정
st.title("전해인의 첫 streamlit 웹🤩")

#텍스트 출력
st.info("파이썬과 streamlit으로 제작한 웹 애플리케이션입니다.")

#사용자 입력 받기
name = st.text_input("이름을 입력해 주세요.")
btn = btn = st.button("등록")


#columns 설정
col1, col2 = st.columns(2)
with col1:
    st.write("제작 날짜: 2026. 10. 27.")
with col2:
    st.write("제작 요일: 수요일")

#버튼 클릭 이벤트
if st.button("인사하기"):
    if name:
        st.success(f"안녕하세요, {name}님!")
    else:
        st.warning("이름을 입력해 주세요.")

#리스트 출력
task = "0"
tasks = [
    "1. streamlit 연습하기"
    "2. streamlit 공부하기"
    "3. 지난 시간에 배운 것 복습하기"
]

st.subheader("※금일 할 일 목록※")

for task in tasks:
    #border=True를 주면 각 반복 요소가 단정한 상자로 감싸짐
    with st.container(border=True):
        st.write(task)

