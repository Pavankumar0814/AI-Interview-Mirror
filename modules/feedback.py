import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_feedback(answer):

    response = model.generate_content(
        f"Give interview feedback for this answer: {answer}"
    )

    return response.text