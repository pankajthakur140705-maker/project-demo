import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        print(f"👤 You said: {text}")
        return text

    except sr.WaitTimeoutError:
        return "No speech detected"
    except sr.UnknownValueError:
        return "Could not understand audio"
    except Exception as e:
        return f"Error: {str(e)}"