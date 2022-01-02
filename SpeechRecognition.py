import pyttsx3
import speech_recognition as sr
import LightControl as lc


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        speech = ""

        try:
            speech = r.recognize_google(audio)
            print(speech)
        except Exception as e:
            print("Exception:", str(e))

    return speech.lower()


WAKE = "hey you"

while 1:
    print("Listening...")
    text = get_text()
    if text.count(WAKE) > 0:
        speak("Hello")
        text = get_text()

        LIGHT_ON_STRS = ["turn on zack's lights", "turn on zach's lights"]
        for phrase in LIGHT_ON_STRS:
            if phrase in text:
                lc.set_power(1)

        LIGHT_OFF_STRS = ["turn off zack's lights", "turn off zach's lights"]
        for phrase in LIGHT_OFF_STRS:
            if phrase in text:
                lc.set_power(0)

        LIGHT_BRIGHT_STRS = ["set the lights to 100"]
        for phrase in LIGHT_BRIGHT_STRS:
            if phrase in text:
                lc.change_brightness(100)
