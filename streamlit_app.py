import streamlit as st

st.set_page_config(
    page_title="AI Interview Mirror",
    page_icon="🎤",
    layout="wide"
)

st.sidebar.title("Features")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Eye Tracking",
        "Emotion Detection",
        "Speech Analysis",
        "Confidence Analysis",
        "Cheating Detection"
    ]
)
if module == "Eye Tracking":
    st.header("Eye Tracking")
    st.info("Run locally for webcam access")

elif module == "Emotion Detection":
    st.header("Emotion Detection")
    st.info("Run locally for webcam access")

elif module == "Speech Analysis":
    st.header("Speech Analysis")
    st.success("Run locally for microphone access")

elif module == "Confidence Analysis":
    st.header("Confidence Analysis")
    st.write("Analyze speaking confidence")

elif module == "Cheating Detection":
    st.header("Cheating Detection")
    st.warning("Detect suspicious movements")