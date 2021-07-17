from playsound import playsound
from gtts import gTTS
import os
import time

questions = ['Hi there', 'Are you ready to answer the questions? Please reply by yes or no',
             'Did you use public transport today?', 'Have you had any contact with a COVID-19 patient?',
             'Do you have COVID-19 symptoms?', 'Are you complying with COVID-19 protocols?',
             'Thank you for answering all the questions. Have a nice day ahead']

please_reply = gTTS(text='Please reply now', lang='en', slow=False)
if 'please-reply.mp3' not in os.listdir('sounds'):
    please_reply.save('sounds/please-reply.mp3')
else:
    playsound('sounds/please-reply.mp3')
playsound('sounds/please-reply.mp3')


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
        i = i + 1
        time.sleep(2)


transcribe()

# trans1 = gTTS(text=q0, lang='en', slow=False)
# if 'trans1.mp3' not in os.listdir('sounds'):
#    trans1.save('sounds/trans1.mp3')
# playsound('sounds/trans1.mp3')
