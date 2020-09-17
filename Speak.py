import pyttsx3

rvoice = pyttsx3.init()
rvoice.setProperty('rate',250)
voices = rvoice.getProperty('voices')
for voice in voices:
    print(voice.id)
    if voice.id != 'com.apple.speech.synthesis.voice.kyoko':
        rvoice.setProperty('voice', voice.id)
        rvoice.say("Hello World")
        rvoice.runAndWait()
