import os
import speech_recognition as sr
import time
from playsound import playsound
from gtts import gTTS

questions = ['Hi there', 'Are you ready to answer the questions? Please reply by yes or no',
             'Did you use public transport today?', 'Have you had any contact with a COVID-19 patient?',
             'Do you have COVID-19 symptoms?', 'Are you complying with COVID-19 protocols?',
             'Thank you for answering all the questions. Have a nice day ahead']

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "favorable-sylph-320123",
  "private_key_id": "7db32c029fd80d0b24902a3c292f9c5d91e779f3",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC/k+nmnQaILMZF\nRnthxwvyndQ0jvR9LxkEoAaiELN/lfKAUnac7sIrokjnWmPf8fp+Mf4loC9yxMc+\nJ6PjhtTpfEUgLkiMGeLqvM5acUyBJuCI15mqkz7d3iSED+guWNRK5OJRBKyuoH6B\n+KdGR5xC//F23pGqinzx8mjCMJ5QIsFw2DYa2V7m26l6ZrjUgQk6Hqph30LM07hY\nBOF9B25ZAjF1oIU6zRh7KWvENIFOHCVzVZsRKDD8SQaNwqzT5NoqNIEJ4UPMGh7j\nT2OXO2L7MxD+ggaXsOB+x+PmnLljGrGJ/nzNg7wiq6TXlj3ejll/dbgNLjU08SDT\nsUvEytzJAgMBAAECggEALhWRvYTmbll+9GkpAvNTv3AR/Paqf3aV6RPppJCp7TYP\n2Kh9mfChSsfGC8kln1hhLnwuK7Tl1RDa8OuuM+xaSTQ4mK4pi3IqsNbsOLtqcOL+\nPkzGzU6QX+SxGgeNjaCWqNF4U47xTyySYgeDjZdqUn+pATQ3DDQ2LClo49W4L4RR\nK1YagiTNUygLRjAV/Q6tpmcpIg+ZgMcXndHERrj1y0Nt+OCdS2YgBCV6nNylEBX+\nBMOuWJ4z7OsvWYNR8J2Z+JsB0nIRxvtzM7LHTy8Cz46Jl3imOd4Hz2sE5vaQox4T\nvjNfCwvKtkEmBIIBBbMn9clXrLicfirqN09ChJeIJQKBgQD/fEowOKe50XA8c/xi\nAQPGAgBQXKJ+G5x42PP09+3uzhoG7JthFTsgKDvjSMgKdGJeyt22FNVYuRGH4V+q\nPe/lGm55V1Crm5dbw2hpEKxUVW5swMrdK6s9BPa20bz2xc0QrBHGuNh/z+oLWUhB\nlvdBf8x80+eXsItlNStanoeOFwKBgQC/9q12l0wCMifiCTPbKugVjiMRfuaMiIuA\n00XT0C6++5k18ielLXzelN1IRQEYtDrnI5fyjmFJyLIK3YN60RKM792BBjYLg7aT\nhvO98Ly4UH59I3yDZCA+E0o6m8alTyK+qPgTAcUbhU8Y9HjMPBcn9klaCxrp/OWO\nYAeb9vWYHwKBgGrdfVbATAAgx/axeU8xJ3fqnGEA7oMbX475CMpd7mtmUGK3E6M/\nMzUXPz2p0ur0lbUa3DRucHMlLl0M+2wFblQBg1ZEHJ07fstGaGUSMVMxTPg2iGSN\nAJqMefosrwL15/niT6k05nJH8JkApoWw9QmzwEAyjvvXP+d8nv7PstnPAoGABSb6\nyucOrDRqa5+xm51QM1voRwzv5S+5BtEk26WHy6p3F0KTm9RXuKWoNstbVy1nM1L6\nPhFiPRe855vAbqhz5gJ+IHtpMe/sE5OYsS1n8059xqAQNHqYfvIHmQEbWM6B8ToZ\nxnDSuIVgdRwCrgCi4niyyU7o/wTBqIudSKtdNiMCgYADC+4Ha7ozOiEruBV97iOo\nOt7UyCWPGYoTX0TOaix84iG4GZklP7Nb5X+stvtBsjd6TWWeq6aLL1ZW0gYgiNks\njdTCRQoDKTiHydqZyTBcavXrrq92K+oIxShX6BBpT4WIM4PIWhfdN6BaqPXc+ey7\nlhuKMSczyje4JCip56hlzA==\n-----END PRIVATE KEY-----\n",
  "client_email": "speech-trial@favorable-sylph-320123.iam.gserviceaccount.com",
  "client_id": "112575634963760049111",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/speech-trial%40favorable-sylph-320123.iam.gserviceaccount.com"
}
"""

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

        i = i + 1
        time.sleep(2)

transcribe()

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    print("Please wait for 1 second")

    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)
    print("Please say something")


