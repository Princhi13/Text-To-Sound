from gtts import gTTS
from playsound import playsound
import time

text_val = input('Текст ')
language = input('Язык ')

obj = gTTS(text=text_val, lang=language, slow=False)
obj.save('sound.mp3')

print('Подождите 3 секунды.')
time.sleep(3)

playsound('sound.mp3')