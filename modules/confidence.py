import speech_recognition as sr
import time

def analyze_confidence():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Speak confidently...")

        start = time.time()

        audio = recognizer.listen(source)

        end = time.time()

        duration = end - start

        text = recognizer.recognize_google(audio)

        print("\nYou said:")
        print(text)

        print("\nSpeaking Time:", round(duration, 2), "seconds")

        # Confidence analysis
        if duration < 3:
            print("Feedback: You spoke too quickly. Try slowing down.")
        elif duration > 10:
            print("Feedback: You spoke slowly. Be more confident.")
        else:
            print("Feedback: Good confidence and speaking speed.")