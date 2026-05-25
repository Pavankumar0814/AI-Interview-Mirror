from modules.emotion_detection import *
from modules.eye_tracking import *
from modules.speech_to_text import *
from modules.feedback import *

print("AI Interview Mirror Started")

detect_emotion()

text = speech_to_text("voice.wav")
print("You said:", text)

feedback = generate_feedback(text)
print(feedback)