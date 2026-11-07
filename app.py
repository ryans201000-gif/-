
st.markdown("""
<style>
.stApp {
    background-color: white;
    color: black;
    background-image:
        radial-gradient(circle, transparent 40%, white 100%);
}

.stApp::before {
    content: "💀     ☠️     💀     ☠️";
    position: fixed;
    inset: 0;
    font-size: 65px;
    line-height: 130px;
    letter-spacing: 25px;
    word-spacing: 20px;
    opacity: 0.13;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
    white-space: pre-wrap;
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
