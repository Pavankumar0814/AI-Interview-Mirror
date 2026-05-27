import cv2
from mediapipe.python import solutions as mp_solutions
import av
mp_face_detection = mp_solutions.face_detection
face_detection = mp_face_detection.FaceDetection()
import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 220px;
    font-size: 18px;
}

.stSelectbox label {
    color: white;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

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
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    results = face_detection.process(img)

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box

            h, w, c = img.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            cv2.rectangle(
                img,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                2
            )

            cv2.putText(
                img,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    return av.VideoFrame.from_ndarray(img, format="bgr24")
if module == "Eye Tracking":
    st.header("Eye Tracking")
    webrtc_streamer(
    key="eye-tracking",
    video_frame_callback=video_frame_callback
)
elif module == "Emotion Detection":
    st.header("Emotion Detection")

    from streamlit_webrtc import webrtc_streamer
    import av
    import cv2
    import mediapipe as mp

    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection()

    def emotion_frame(frame):
        img = frame.to_ndarray(format="bgr24")

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb)

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box

                h, w, _ = img.shape

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                bw = int(bbox.width * w)
                bh = int(bbox.height * h)

                cv2.rectangle(img, (x, y), (x+bw, y+bh), (0,255,0), 2)

                cv2.putText(
                    img,
                    "Emotion: Neutral",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2
                )

        return av.VideoFrame.from_ndarray(img, format="bgr24")

    webrtc_streamer(
        key="emotion",
        video_frame_callback=emotion_frame
    )

elif module == "Speech Analysis":
    st.header("Speech Analysis")

    import speech_recognition as sr

    recognizer = sr.Recognizer()

    if st.button("Start Listening"):

        with sr.Microphone() as source:

            st.write("Listening... Speak now")

            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)

                st.success("You said:")
                st.write(text)

            except:
                st.error("Could not understand audio")

elif module == "Confidence Analysis":

    st.header("Confidence Analysis")

    import speech_recognition as sr
    import time

    recognizer = sr.Recognizer()

    if st.button("Analyze Confidence"):

        with sr.Microphone() as source:

            st.write("Speak for a few seconds...")

            start = time.time()

            audio = recognizer.listen(source)

            end = time.time()

            duration = end - start

            try:

                text = recognizer.recognize_google(audio)

                st.success("You said:")
                st.write(text)

                st.write(f"Speaking Time: {round(duration,2)} seconds")

                if duration < 3:
                    st.error("Low Confidence: You spoke too fast")

                elif duration > 10:
                    st.warning("Slow Speaking: Try speaking confidently")

                else:
                    st.success("Good Confidence and speaking speed")

            except:
                st.error("Could not understand audio")

elif module == "Cheating Detection":

    st.header("Cheating Detection")

    from streamlit_webrtc import webrtc_streamer
    import av
    import cv2
    import mediapipe as mp

    mp_face_mesh = mp.solutions.face_mesh

    face_mesh = mp_face_mesh.FaceMesh(
        refine_landmarks=True
    )

    def cheating_detection(frame):

        img = frame.to_ndarray(format="bgr24")

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb)

        h, w, _ = img.shape

        status = "Looking Forward"

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:

                nose = face_landmarks.landmark[1]

                nose_x = int(nose.x * w)

                cv2.circle(img, (nose_x, 200), 5, (0,255,0), -1)

                if nose_x < w * 0.35:
                    status = "Looking Left"

                elif nose_x > w * 0.65:
                    status = "Looking Right"

                else:
                    status = "Looking Forward"

                cv2.putText(
                    img,
                    status,
                    (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3
                )

        return av.VideoFrame.from_ndarray(img, format="bgr24")

    webrtc_streamer(
        key="cheating",
        video_frame_callback=cheating_detection
    )