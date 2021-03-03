import speech_recognition
import pyttsx3
from datetime import date, datetime

ai_ear = speech_recognition.Recognizer()
ai_mouth = pyttsx3.init()
ai_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("I'm listening")
        audio = ai_ear.listen(mic)

    print("...")

    try:
        you = ai_ear.recognize_google(audio)
    except:
        you == ""
    print ("You: " +you)

    if you == "":
        ai_brain = " i can't hear you, try again,please!"
    elif  "hello" in you:
        ai_brain =  "hello!"
    elif "today" in you:
        today = date.today()
        ai_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        ai_brain =  now.strftime("%H hours %M minutes %S seconds")
    elif "emperor" in you:
        ai_brain = "Hirohito"
    elif "bye" in you:
        ai_brain = "bye!"
        print(ai_brain)
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        break
    else:
        ai_brain="Sorry, i don't understand."

print("Ai: " +ai_brain)
ai_mouth.say(ai_brain)
ai_mouth.runAndWait()