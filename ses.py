from gtts import gTTS
import os 

text = 'Türk Hack Team, Türkiyenin önde gelen siber güvenlik sayfasıdır'  
language = 'tr' 


speech = gTTS(text = text, lang = language, slow = False)   

speech.save("tht.mp3")  

os.system("start tht.mp3")      