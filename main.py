# Virtual Assistant named Alfred
# by: Arman Nadjarian
# 1/13/2022

# Boiler plate code used in the creation of this project can be found at:
#       https://pypi.org/project/SpeechRecognition/1.2.3/

# Purpose:
#   The purpose of this project is to learn how to interact with hardware via Python.
#   Additionally, to learn how to take data from peripherals and perform analysis on said data.
#   This project is a virtual assistant that is able to respond to user voice commands


# Through the speech_recognition Python module, I am able to implement Google's voice recognition
# software in order to gather microphone data and perform the functions of a Virtual Assistant.

# Command line instruction to run the program:
#           python3 main.py


import speech_recognition
import webbrowser


# execute_command(command: str)
# Commands will be cross referenced with available list of commands
# If command is found, it will be performed
# if command is not found, the appropriate message will display

def execute_command(command: str):
    command = command.lower()

    if command.lower() == "introduce yourself":
        print("Hello, my name is Alfred...")
        print("Your virtual assistant.")

    # checks if web browser command was entered
    elif command.lower() == "open google":
        print("Opening Google...")
        webbrowser.open("https://google.com", new=2)

    else:
        print("Command not found...")


def main():
    magic_word = "Terminate"  # phrase that will terminate the program if said
    recognizer = speech_recognition.Recognizer()

    pattern = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

    while True:
        print("\n" + pattern)
        input("Press Enter to say a command...\n")
        print(f"Say something... Or say \"{magic_word}\" to end the program's execution...")

        # listen on the system's default microphone
        with speech_recognition.Microphone() as mic:
            input_audio = recognizer.listen(mic)

        try:
            # Google's speech recognition algorithm is used to match audio input to English words
            spoken_text = recognizer.recognize_google(input_audio)

            # printing command
            print("\nCommand: \"" + spoken_text + "\"\n")

            spoken_text = spoken_text.lower()

            #########################################################################################################

            # Here is where inputted commands will be checked against the current voice features available...
            # checking for magic word

            if spoken_text == magic_word.lower():
                print("\nYou used the magic word. Terminating program...")
                print(pattern)
                exit(0)

            execute_command(spoken_text)

            print(pattern)

        except LookupError:
            print("\nException occurred. Breaking execution...")


if __name__ == "__main__":
    main()
