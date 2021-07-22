import os
import speech_recognition as sr
import time
from playsound import playsound
from gtts import gTTS
import json
import xlrd
from xlwt import Workbook
from delete_file import deleteFile

deleteFile()

questions = ['Hi there', 'Are you ready to answer the questions?',
             'Did you use public transport today?', 'Have you had any contact with a COVID-19 patient?',
             'Do you have COVID-19 symptoms?', 'Are you complying with COVID-19 protocols?',
             'Thank you for answering all the questions. Have a nice day ahead']

r = sr.Recognizer()
m = sr.Microphone()

# Google Authentication

google_json = json.load(open('google.json'))
GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.dumps(google_json)

# replies

reply = gTTS(text='Please reply by yes or no after the beep', lang='en', slow=False)
reply_wrong = gTTS(text='Please only reply by yes or no', lang='en', slow=False)
reply_unable = gTTS(text='Unable to register your response.', lang='en', slow=False)

############################################

if 'please-reply.mp3' not in os.listdir('sounds'):
    reply.save('sounds/please-reply.mp3')
else:
    reply.save('sounds/please-reply.mp3')

if 'reply_wrong.mp3' not in os.listdir('sounds'):
    reply.save('sounds/reply_wrong.mp3')
else:
    reply.save('sounds/reply_wrong.mp3')

if 'reply_unable.mp3' not in os.listdir('sounds'):
    reply.save('sounds/reply_unable.mp3')
else:
    reply.save('sounds/reply_unable.mp3')

############################################

wb2 = Workbook()
sheet1 = wb2.add_sheet('sheet 1')


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error in creating directory: ' + directory)


createFolder('excel')

if 'compliance_form.xls' not in os.listdir('excel'):
    for j in range(5):
        sheet1.col(j).width = 5000
    sheet1.write(0, 0, 'Ready')
    sheet1.write(0, 1, 'Public transport')
    sheet1.write(0, 2, 'Contact with infected')
    sheet1.write(0, 3, 'Symptoms')
    sheet1.write(0, 4, 'Compliance with protocols')
    wb2.save('excel/compliance_form.xls')
else:
    pass


def transcribe():
    i = 0
    for question in questions:
        sI = str(i)
        trans = gTTS(text=question, lang='en', slow=False)
        if 'trans.mp3' not in os.listdir('sounds'):
            trans.save('sounds/trans-' + sI + '.mp3')
            playsound('sounds/trans-' + sI + '.mp3')
        else:
            playsound('sounds/trans-' + sI + '.mp3')
        if i != 0 and i != 6:
            time.sleep(0.3)
            playsound('sounds/please-reply.mp3')
            with m as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                playsound('sounds/start-beep.wav')
                audio = r.listen(source)
            try:
                print(
                    "Your answer is " +
                    r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
                replyFunction(i, audio)

            except sr.UnknownValueError:
                playsound('sounds/fail-beep.wav')
                print('I could not understand what you just said.\nPlease try again')
                time.sleep(0.3)
                try:
                    time.sleep(0.3)
                    playsound('sounds/start-beep.wav')
                    print(
                        'Did you say ' + r.recognize_google_cloud(audio,
                                                                  credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
                    replyFunction(i, audio)

                except sr.UnknownValueError:
                    time.sleep(0.3)
                    playsound('sounds/fail-beep.wav')
                    time.sleep(0.5)
                    playsound('sounds/reply_unable.mp3')
                    print('I still cannot understand what you just said.')
                    pass
                except sr.RequestError as e:
                    time.sleep(0.3)
                    playsound('sounds/fail-beep.wav')
                    print('Could not fetch results from Google Cloud Speech services; {0}'.format(e))
            except sr.RequestError as e:
                time.sleep(0.5)
                playsound('sounds/fail-beep.wav')
                print('Could not fetch results from Google Cloud Speech services; {0}'.format(e))
        else:
            pass
        i = i + 1

    time.sleep(1)


def replyFunction(j, audio1):
    if r.recognize_google_cloud(audio1,
                                credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS) == 'no' or 'No' or 'nah' or 'Nah':
        sheet1.write(1, j - 1, 'N')
        wb2.save('excel/compliance_form.xls')
        print('\nResponse saved.\n')
        time.sleep(0.3)

    elif r.recognize_google_cloud(audio1,
                                  credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS) == 'yes' or 'Yes' or 'yeah' or 'Yeah':
        sheet1.write(1, j - 1, 'Y')
        wb2.save('excel/compliance_form.xls')
        print('\nResponse saved.\n')
        time.sleep(0.3)

    else:
        playsound('sounds/reply_wrong.mp3')
        replyFunction(j, audio1)


transcribe()
