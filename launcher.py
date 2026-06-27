from core.startup import Startup
from core.assistant import Assistant

if __name__ == "__main__":
    startup = Startup()
    startup.boot()

    assistant = Assistant()
    assistant.start()

    print("LOLAH is running. Type something...")

    while True:
        user_input = input("You: ")
        response = assistant.process(user_input)
        print("Lolah:", response)
