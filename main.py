import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound
import os
import random
import musicLibrary

def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    filename = f"voice{random.randint(1,99999)}.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def pressCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif c.startswith("play"):
        song = c.replace("play", "").strip()  # FIXED multi-word song names

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have the song {song} in my library.")
    elif c.startswith("search"):
        query = c.replace("search", "").strip()
        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What should I search for?")
    elif "open notepad" in c:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open calculator" in c:
        speak("Opening Calculator")
        os.system("calc")
    elif "open paint" in c:
        speak("Opening Paint")
        os.system("mspaint")
    elif "open command prompt" in c:
        speak("Opening Command Prompt")
        os.system("cmd")

    # --- Folders ---
    elif "open documents" in c:
        speak("Opening Documents folder")
        os.system("explorer %userprofile%\\Documents")
    elif "open downloads" in c:
        speak("Opening Downloads folder")
        os.system("explorer %userprofile%\\Downloads")
    elif "open desktop" in c:
        speak("Opening Desktop")
        os.system("explorer %userprofile%\\Desktop")

    # --- System Control ---
    elif "shutdown" in c:
        speak("Shutting down the computer")
        os.system("shutdown /s /t 1")
    elif "restart" in c:
        speak("Restarting the computer")
        os.system("shutdown /r /t 1")
    elif "log off" in c:
        speak("Logging off")
        os.system("shutdown /l")
    elif "lock screen" in c:
        speak("Locking the computer")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    # --- Time / Info ---
    elif "time" in c:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "date" in c:
        from datetime import datetime
        today = datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    # --- Exit Jarvis ---
    elif "exit" in c or "quit" in c:
        speak("Goodbye!")
        os._exit(0)

if __name__ == "__main__":
    speak("Initializing Jarvis")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            word = recognizer.recognize_google(audio).lower()
            print("Heard:", word)

            if word == "jarvis":
                speak("Yes sir?")
                print("Jarvis activated...")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                pressCommand(command)

        except sr.UnknownValueError:
            # Speech not understood
            pass

        except sr.WaitTimeoutError:
            # Silence timeout
            pass

        except Exception as e:
            print("Error:", e)