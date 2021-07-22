import os
import speech_recognition as sr
import time
from playsound import playsound
from gtts import gTTS
import json

questions = ['Hi there', 'Are you ready to answer the questions?',
             'Did you use public transport today?', 'Have you had any contact with a COVID-19 patient?',
             'Do you have COVID-19 symptoms?', 'Are you complying with COVID-19 protocols?',
             'Thank you for answering all the questions. Have a nice day ahead']

r = sr.Recognizer()
m = sr.Microphone()

# Google Authentication

google_json = json.load(open('google.json'))
GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.dumps(google_json)

reply = gTTS(text='Please reply by yes or no after the beep', lang='en', slow=False)

if 'please-reply.mp3' not in os.listdir('sounds'):
    reply.save('sounds/please-reply.mp3')
else:
    reply.save('sounds/please-reply.mp3')


def transcribe():
    i = 0
    for question in questions:
        sI = str(i)
        trans = gTTS(text=question, lang='en', slow=False)
        if 'trans.mp3' not in os.listdir('sounds'):
            trans.save('sounds/trans-' + sI + '.mp3')
        else:
            playsound('sounds/trans-' + sI + '.mp3')
        playsound('sounds/trans-' + sI + '.mp3')
        if i != 0 and i != 6:
            time.sleep(0.5)
            playsound('sounds/please-reply.mp3')
            with m as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                playsound('sounds/start-beep.wav')
                audio = r.listen(source)
            try:
                print(
                    "Did you say " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
            except sr.UnknownValueError:
                playsound('sounds/fail-beep.wav')
                print('I could not understand what you just said.\nPlease try again')
                time.sleep(0.5)
                try:
                    time.sleep(0.5)
                    playsound('sounds/start-beep.wav')
                    print(
                        'Did you say ' + r.recognize_google_cloud(audio,
                                                                  credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
                except sr.UnknownValueError:
                    time.sleep(0.5)
                    playsound('sounds/fail-beep.wav')
                    print('I still cannot understand what you just said.')
            except sr.RequestError as e:
                time.sleep(0.5)
                playsound('sounds/fail-beep.wav')
                print('Could not fetch results from Google Cloud Speech services; {0}'.format(e))
        else:
            pass
        i = i + 1
        time.sleep(2)


transcribe()
