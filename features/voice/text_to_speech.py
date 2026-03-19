import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text: str):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)