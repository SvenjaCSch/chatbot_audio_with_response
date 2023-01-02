import datetime
import pyttsx3
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import time
time.clock = time.time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

chatbot = ChatBot("Speaker")
trainer = ListTrainer(chatbot)

trainer.train(
    'C:/Users/svcsc/Desktop/Code/archive'
)

exit_conditions = (":q", "quit", "exit", "bye", "ciao", "see you", "I have to go")

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What do you what to know?")
        audio = r.listen(source)
        try:
            said_words = r.recognize_google(audio)
            print("You said:- " + said_words)
            if said_words in exit_conditions:
                break
            else:
                print(f"{chatbot.get_response(said_words)}")
        except sr.UnknownValueError:
            print("Could not understand a word.")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
