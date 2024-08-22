# Message Reminder Program .............//////////////

import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech

while True:
    message = "Hello,How are you!"
    engine.say(message)
    engine.runAndWait()
    time.sleep(10)
