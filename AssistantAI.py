import speech_recognition
import pyttsx3

#initiate listening and speaking skill
rvoice = pyttsx3.init()
rvoice.setProperty('rate',250)
robot_ear = speech_recognition.Recognizer()


assistant_brain = "I'm listening"
rvoice.say(assistant_brain)
print(assistant_brain)
#rvoice.runAndWait()

while True:
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print(you)

    if you == "":
        assistant_brain = "Did you say something"
    elif you == "hello":
        assistant_brain = "Hello buddy"
    elif you == "thank you":
        assistant_brain = "Cool, anything else"
    elif you == "bye":
        assistant_brain = "bye"
        print(assistant_brain)    
        rvoice.say(assistant_brain)
        rvoice.runAndWait()
        break
    else:
        assistant_brain = "You can google it youself"


    print(assistant_brain)    
    rvoice.say(assistant_brain)
    rvoice.runAndWait()
