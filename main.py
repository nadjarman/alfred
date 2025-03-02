""" Virtual Assistant named Alfred

    by: Arman Nadjarian
    Date of Creation: 1/13/2022
"""

import speech_recognition
from search import open_google, search_for


def execute_command(command: str) -> None:
    """ Executes the passed in command

    Args:
        command (str): the command string to be executed
    """

    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        command = command.lower()

        if command.lower() == "introduce yourself":
            print("Hello, my name is Alfred...")
            print("Your virtual assistant.")

        # checks if web browser command was entered
        elif command.lower() == "open google":
            open_google()
        elif command.lower() == "google search":
            try:
                print("Say your desired search phrase...")
                input_audio = recognizer.listen(mic)
                search_term = recognizer.recognize_google(input_audio)
                search_for(search_term)
            except (LookupError, speech_recognition.UnknownValueError):
                print("\nException occurred. Breaking execution...")
                exit(0)
        else:
            print("Command not found...")


def main() -> None:
    """ Entry point """

    magic_word = "Terminate"  # phrase that will terminate the program if said
    recognizer = speech_recognition.Recognizer()

    pattern = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

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

            ########################################################################################

            # Here is where inputted commands will be checked against the current
            # voice features available...

            if spoken_text == magic_word.lower():
                print("\nYou used the magic word. Terminating program...")
                print(pattern)
                exit(0)

            execute_command(spoken_text)

            print(pattern)

        except (LookupError, speech_recognition.UnknownValueError):
            print("\nException occurred. Breaking execution...")
            exit(0)


if __name__ == "__main__":
    main()
