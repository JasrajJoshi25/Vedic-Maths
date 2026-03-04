import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    """Speak out the command"""
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Good Afternoon sir,how may i help you?")
    # print(voices)