from core.memory import Memory
from core.orchestrator import Assistant
from features.voice.speech_to_text import listen
from features.voice.text_to_speech import speak

def main():
    print("🌾 AI Rural Assistant (Advanced) Started\n")

    memory = Memory()
    assistant = Assistant(memory)

    while True:
        mode = input("\nChoose input: (t) text | (s) speech | (exit): ")

        if mode == "exit":
            print("👋 Exiting...")
            break

        if mode == "s":
            user_input = listen()
        else:
            user_input = input("You: ")

        if not user_input:
            continue

        response = assistant.process(user_input)

        print("\n🤖 AI:", response)
        speak(response)


if __name__ == "__main__":
    main()