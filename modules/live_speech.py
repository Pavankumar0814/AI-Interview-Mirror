import speech_recognition as sr
from feedback import generate_feedback

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("Speak now...")

    audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio)

    print("\nYou said:")
    print(text)

    print("\nAI Feedback:\n")

    feedback = generate_feedback(text)

    print(feedback)