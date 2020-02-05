#importing speech recognition; sr is shorten for speech recognition
import speech_recognition as sr

#r equal recognizer
r = sr.Recognizer()

#using a microphone as a source
with sr.Microphone() as source:
    #saying print will make it type "Say something" in the console
    print("Say something")
    #setting the audio to the recognizer object with the listen method and connect it to the microphone(source)
    audio = r.listen(source)