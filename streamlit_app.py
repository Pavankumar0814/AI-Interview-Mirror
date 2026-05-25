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
    st.write("Eye tracking module")

elif feature == "Emotion Detection":
    st.write("Emotion detection module")

elif feature == "Speech Analysis":
    st.write("Speech analysis module")

elif feature == "Confidence Analysis":
    st.write("Confidence analysis module")

elif feature == "Cheating Detection":
    st.write("Cheating detection module")