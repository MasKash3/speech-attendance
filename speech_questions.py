import os
import speech_recognition as sr
import time
from playsound import playsound
from gtts import gTTS
import json

questions = ['Hi there', 'Are you ready to answer the questions? Please reply by yes or no',
             'Did you use public transport today?', 'Have you had any contact with a COVID-19 patient?',
             'Do you have COVID-19 symptoms?', 'Are you complying with COVID-19 protocols?',
             'Thank you for answering all the questions. Have a nice day ahead']

r = sr.Recognizer()
m = sr.Microphone()

# Google Authentication

#f = open('google.json', 'r')
#json_data = []
#data = json.load(f)
#json_data.append(data)
#print(json_data[0])
GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.load(open('google.json'))
print(GOOGLE_CLOUD_SPEECH_CREDENTIALS)

reply = gTTS(text='Please reply now', lang='en', slow=False)
if 'please-reply.mp3' not in os.listdir('sounds'):
    reply.save('sounds/please-reply.mp3')
else:
    pass


def transcribe():
    i = 0
    for question in questions:
        sI = str(i)
        trans = gTTS(text=question, lang='en', slow=False)
        if 'trans.mp3' not in os.listdir('sounds'):
            trans.save('sounds/trans' + sI + '.mp3')
        else:
            playsound('sounds/trans' + sI + '.mp3')
        playsound('sounds/trans' + sI + '.mp3')
        if i != 0:
            time.sleep(0.5)
            playsound('sounds/please-reply.mp3')
            with m as source:
                # print("Please wait for 1 second")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
            try:
                print("Did you say " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
            except sr.UnknownValueError:
                print('I could not understand what you just said.\nPlease try again')
                try:
                    print(
                        'Did you say ' + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
                except sr.UnknownValueError:
                    print('I still cannot understand what you just said.')
            except sr.RequestError as e:
                print('Could not fetch results from Google Cloud Speech services; {0}'.format(e))
        else:
            pass
        i = i + 1
        time.sleep(2)


transcribe()

print("Please say something")
