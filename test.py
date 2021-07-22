import json

GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.load(open('google.json'))
print(GOOGLE_CLOUD_SPEECH_CREDENTIALS)
print('\n')
y = json.dumps(GOOGLE_CLOUD_SPEECH_CREDENTIALS)

print(y)