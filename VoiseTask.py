from __future__ import print_function
from email.mime import audio
from re import L
import speech_recognition
from datetime import datetime
import time
import os
import shutil


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

date = datetime.now().date()
time = datetime.now().time()

input('Нажмите Enter, чтобы начать запись...')
print('Что добавить в заметки?')

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    qwery = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

input(f'{qwery}\nНажмите Enter, чтобы сохранить запись.')
    
with open('VoiseTask.txt', 'a') as file:
    file.write(f'{date} {time.hour}:{time.minute} - {qwery}.\n')
    print(f'Заметка сохранена!')
    exit()






    




