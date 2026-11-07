
import streamlit as st
import time

st.set_page_config(page_title="Welcome", page_icon="💣")

st.markdown("""
<style>
.stApp {
    background-color: white;
    color: black;
}
h1, p {
    color: black !important;
    text-align: center;
}
.stButton {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("<h1>어서 오세요!</h1>", unsafe_allow_html=True)

    if st.button("들어가기"):
        st.session_state.started = True
        st.rerun()
else:
    st.markdown("""
    <div style="text-align:center; padding-top:100px;">
        <h1 style="font-size:45px;">
            하하하 걸렸구나!!
        </h1>
        <div style="font-size:100px; animation: boom 0.5s infinite alternate;">
            💥
        </div>
    </div>

    <style>
    @keyframes boom {
        from {transform: scale(0.5); opacity: 0.4;}
        to {transform: scale(1.5); opacity: 1;}
    }
    </style>
    """, unsafe_allow_html=True)
