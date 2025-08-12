
import os
import streamlit as st

# Optional: pandas only if you want to demo tables later
try:
    import pandas as pd  # noqa: F401
except Exception:
    pass

st.set_page_config(page_title="SsamM_test1 - Gemini Demo", page_icon="✨", layout="wide")
st.title("✨ Gemini API 연동 Streamlit 데모")

st.write("GitHub → Streamlit 배포 + **Google Gemini** API 연동 예시입니다. "
         "좌측에서 파라미터를 설정하고 프롬프트를 보내보세요.")

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "Model",
        ["gemini-1.5-flash", "gemini-1.5-pro"],
        index=0
    )
    temperature = st.slider("temperature", 0.0, 2.0, 0.7, 0.1)
    max_output_tokens = st.slider("max_output_tokens", 64, 4096, 512, 64)
    st.markdown("---")
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if api_key:
        st.success("GOOGLE_API_KEY: 감지됨 ✅")
    else:
        st.warning("GOOGLE_API_KEY가 없습니다. 배포 전 Streamlit Secrets에 추가하세요.")

# ---------------- Tabs ----------------
tab1, tab2 = st.tabs(["📝 Text Generation", "🧪 Prompt Playground"])

# Utility: lazy import for the SDK (avoids import errors before requirements installed)
def get_gemini_client():
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    return genai

# ---- Tab1: simple text generation
with tab1:
    st.subheader("📝 프롬프트 → 텍스트 생성")
    prompt = st.text_area(
        "프롬프트 입력",
        value="서울의 주말 날씨를 친근한 톤으로 3문장 요약해줘 (예시).",
        height=140
    )
    if st.button("Generate", key="gen1"):
        if not api_key:
            st.error("GOOGLE_API_KEY가 없습니다. 좌측 안내를 참고해 Secrets에 추가한 뒤 다시 시도하세요.")
        else:
            try:
                genai = get_gemini_client()
                generation_config = {
                    "temperature": temperature,
                    "max_output_tokens": max_output_tokens,
                }
                model_obj = genai.GenerativeModel(model_name=model, generation_config=generation_config)
                with st.spinner("모델 호출 중…"):
                    response = model_obj.generate_content(prompt)
                if response and response.text:
                    st.success("✅ 응답 수신")
                    st.markdown(response.text)
                else:
                    st.warning("응답이 비어있습니다.")
            except Exception as e:
                st.exception(e)

# ---- Tab2: system style + history (basic chat-like)
with tab2:
    st.subheader("🧪 시스템 스타일 + 대화형 테스트")
    system_instruction = st.text_area(
        "System Instruction (선택)",
        value="You are a helpful assistant for English speaking practice. Respond briefly unless asked for details.",
        height=100
    )
    user_input = st.text_area("User Message", value="여행 영어 회화에서 공항 체크인 상황을 5문장으로 역할극 형태로 만들어줘.", height=130)
    col_a, col_b = st.columns(2)
    with col_a:
        keep_history = st.checkbox("히스토리 유지(간단)", value=True)
    with col_b:
        clear = st.button("대화 초기화")

    if "chat_history" not in st.session_state or clear:
        st.session_state.chat_history = []

    if st.button("Send", key="gen2"):
        if not api_key:
            st.error("GOOGLE_API_KEY가 없습니다. 좌측 안내를 참고해 Secrets에 추가한 뒤 다시 시도하세요.")
        else:
            try:
                genai = get_gemini_client()
                generation_config = {
                    "temperature": temperature,
                    "max_output_tokens": max_output_tokens,
                }
                # Build messages: Gemini SDK uses content parts. We'll just join for simplicity.
                messages = []
                if system_instruction.strip():
                    messages.append({"role": "user", "parts": [f"[SYSTEM]: {system_instruction.strip()}"]})
                # past messages
                if keep_history and st.session_state.chat_history:
                    messages.extend(st.session_state.chat_history)
                messages.append({"role": "user", "parts": [user_input]})

                model_obj = genai.GenerativeModel(model_name=model, generation_config=generation_config)
                with st.spinner("모델 호출 중…"):
                    # Use responses API for multi-turn by passing history as 'contents'
                    response = model_obj.generate_content(contents=messages)
                text = getattr(response, "text", None)
                if text:
                    st.session_state.chat_history = messages + [{"role": "model", "parts": [text]}]
                    st.success("✅ 응답 수신")
                    st.markdown(text)
                else:
                    st.warning("응답이 비어있습니다.")
            except Exception as e:
                st.exception(e)

st.markdown("---")
st.caption("ⓒ 2025 SsamM_test1 - Streamlit + Gemini Demo")
