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
    from modules.eye_tracking import track_eyes

if st.button("Start Eye Tracking"):
    track_eyes()

elif feature == "Emotion Detection":
    from modules.emotion_detection import detect_emotion

if st.button("Start Emotion Detection"):
    detect_emotion()

elif feature == "Speech Analysis":
   from modules.speech_to_text import speech_to_text

if st.button("Start Speech Analysis"):
    speech_to_text()

elif feature == "Confidence Analysis":
    from modules.confidence import analyze_confidence

if st.button("Start Confidence Analysis"):
    analyze_confidence()

elif feature == "Cheating Detection":
    from modules.cheating_detection import detect_cheating

if st.button("Start Cheating Detection"):
    detect_cheating()