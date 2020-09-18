import speech_recognition
import pyttsx3

#initiate listening and speaking skill
robot_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()

def onEnd(name, completed):
   print 'finishing', name, completed
   if name == 'start':
      while True:
         with speech_recognition.Microphone() as mic:
            audio = robot_ear.listen(mic)
         try:
            you = robot_ear.recognize_google(audio)
         except:
            you = ''
         print(you)

         if you == '':
            assistant_brain = 'Did you say something'
         elif you == 'hello':
            assistant_brain = 'Hello buddy'
         elif you == 'bye':
            assistant_brain = 'goodbye'
            print(assistant_brain)    
            engine.say(assistant_brain, 'bye')
            engine.runAndWait()
            break
         else:
            assistant_brain = 'I do not know'
         print(assistant_brain)
         engine.say(assistant_brain, 'dog')
   elif name == 'bye':
      engine.say('good ye', 'end')
   elif name == 'end':
      engine.endLoop()
engine = pyttsx3.init()
#engine.connect('started-utterance', onStart)
#engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('Hello world', 'start')
engine.startLoop()