# Jarvis
Jarvis is a voice-activated virtual assistant designed to perform tasks such as web browsing, playing music, search content on google, open system applications and handle other functionalities. 
# Libraries
On the command line, running **pip install -r requirements.txt** will read the file and install each listed library (with the specified version constraints) into the currently active Python environment, which should ideally be a virtual environment.
# Specifications
Voice Recognition
Utilizes the speech_recognition library to listen for and recognize voice commands.
Activates upon detecting the wake word "Jarvis."
Text-to-Speech
Uses gTTS (Google Text-to-Speech) and pygame for playback.
Web Browsing.
Opens websites like Google, Facebook, YouTube based on voice commands.
Music Playback
Interfaces with a musicLibrary module to play songs via web links.
Acts as a general virtual assistant similar to Alexa or Google Assistant.
Activates upon detecting the wake word "Jarvis."
# Work Flow
Initialization
2. Greets the user with "Initializing Jarvis...."
3. Wake Word Detection
4. Listens for the wake word "jarvis."
5. Acknowledges activation by saying "Yes sir"
6. Command Processing and displaying it on the console.
7. Processes commands to determine actions such as opening a website, playing music, opening system apps and performing a google search
8. Speech Output.
9. Provides responses using speak function with gTTS.
