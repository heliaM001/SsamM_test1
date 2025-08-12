
import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="SsamM_test1",
    page_icon="📊",
    layout="centered"
)

# 제목
st.title("📊 SsamM_test1 Streamlit App")

# 소개
st.write("""
이 앱은 **GitHub → Streamlit** 배포 테스트용입니다.  
아래에 간단한 기능 예시를 넣어두었습니다.
""")

# 입력 박스
name = st.text_input("이름을 입력하세요:")

if name:
    st.success(f"안녕하세요, {name}님! Streamlit 앱에 오신 것을 환영합니다.")

# 숫자 입력 & 계산 예시
number = st.number_input("숫자를 입력하세요:", min_value=0, max_value=100, value=10)
st.write(f"{number}의 제곱은 **{number**2}** 입니다.")

# 데이터프레임 예시
df = pd.DataFrame({
    "이름": ["A", "B", "C"],
    "점수": [85, 90, 78]
})
st.subheader("샘플 데이터")
st.dataframe(df)

st.write("---")
st.caption("ⓒ 2025 SsamM_test1 - Streamlit 배포 테스트")
