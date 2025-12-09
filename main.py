# Import necessary libraries
import speech_recognition as sr
import webbrowser  # Fixed typo
import pyttsx3
import google.cloud
import musiclibrary
import client  # Import the Gemini API module
import pyaudio
import google
 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process commands
def process_command(command):
    command = command.lower()  # Normalize the input

    # Predefined commands
    if command == 'open google':
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif command == 'open youtube':
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif command == 'open facebook':
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif command == 'open instagram':
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif command == 'open abrar':
        webbrowser.open("https://www.youtube.com/@WildlensbyAbrar")
        speak("Opening Abrar's channel")
    elif command == 'open techno':
        webbrowser.open("https://www.youtube.com/@TechnoGamerzOfficial")
        speak("Opening Techno Gamerz")
    elif 'play' in command:
        speak("Playing music from your library")
        song_name = command.replace("play", "").strip()
        if song_name in musiclibrary.music:
            link = musiclibrary.music[song_name]
            webbrowser.open(link)
            speak(f"Playing {song_name}")
        else:
            speak("Sorry, I did not understand this command.")

    # If command is not recognized, ask Gemini
    else:
        speak("Let me check...")
        gemini_response = client.ask_gemini(command)  # Call Gemini API
        speak(gemini_response)  # Jarvis speaks Gemini's response


# Main program
if __name__ == "__main__":
    recognizer.energy_threshold = 300  # Adjust for background noise
    recognizer.dynamic_energy_threshold = True  # Dynamically adjust to environment
    speak("Initializing Jarvis")  # Jarvis introduces itself

    while True:  # Infinite loop to keep listening
        try:
            # Listen for the wake word
            with sr.Microphone() as source:
                print("Listening ...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                wake_word = recognizer.recognize_google(audio).lower() # type: ignore

            if wake_word == "yes":
                speak("Yes, I am ready")  # Wake word recognized

                # Listen for the actual command
                print("Listening for command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)
                    command = recognizer.recognize_google(audio) # type: ignore

                # Process the command
                process_command(command)

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except Exception as e:
            print(f"An error occurred: {e}")
