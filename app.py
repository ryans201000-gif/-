
import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="💀",
    layout="centered"
)

if "started" not in st.session_state:
    st.session_state.started = False

st.markdown("""
<style>
.stApp {
    background-color: white;
    color: black;
}

/* 해골 배경 */
.stApp::before {
    content: "💀     ☠️     💀     ☠️     💀";
    position: fixed;
    inset: 0;
    font-size: 55px;
    line-height: 130px;
    letter-spacing: 25px;
    word-spacing: 20px;
    opacity: 0.12;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

/* 콘텐츠 */
.main .block-container {
    position: relative;
    z-index: 1;
    text-align: center;
    padding-top: 100px;
}

h1, p {
    color: black !important;
}

/* 버튼 */
.stButton button {
    background-color: white;
    color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size: 20px;
    padding: 10px 35px;
}

.stButton button:hover {
    background-color: black;
    color: white;
}

/* 폭발 효과 */
@keyframes boom {
    0% {
        transform: scale(0.2);
        opacity: 0;
    }
    50% {
        transform: scale(1.5);
        opacity: 1;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}

.explosion {
    font-size: 110px;
    animation: boom 0.8s ease-out;
}

.message {
    font-size: 45px;
    font-weight: bold;
    color: black;
    animation: boom 0.8s ease-out;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state.started:

    st.markdown("<h1>어서 오세요!</h1>", unsafe_allow_html=True)

    if st.button("들어가기"):
        st.session_state.started = True
        st.rerun()

else:

    st.markdown("""
    <div class="message">
        하하하 걸렸구나!!
    </div>

    <div class="explosion">
        💥
    </div>
    """, unsafe_allow_html=True)
