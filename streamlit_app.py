import streamlit as st

st.set_page_config(page_title="AI Interview Mirror", layout="wide")

st.title("🎤 AI Interview Mirror")

st.sidebar.header("Features")

feature = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "Eye Tracking",
        "Emotion Detection",
        "Speech Analysis",
        "Confidence Analysis",
        "Cheating Detection"
    ]
)

if feature == "Home":
    st.write("Welcome to AI Interview Mirror")

elif feature == "Eye Tracking":
    st.subheader("Eye Tracking")
    st.success("Run locally in VS Code for webcam access")

elif feature == "Emotion Detection":
    st.subheader("Emotion Detection")
    st.success("Run locally in VS Code for camera access")

elif feature == "Speech Analysis":
    st.subheader("Speech Analysis")
    st.success("Run locally for microphone access")

elif feature == "Confidence Analysis":
    st.subheader("Confidence Analysis")
    st.success("Run locally in Python environment")

elif feature == "Cheating Detection":
    st.subheader("Cheating Detection")
    st.success("Run locally for webcam monitoring")