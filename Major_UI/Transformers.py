import torch
import eyed3
import os
import time
from gtts import gTTS
import datetime
import soundfile as sf
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
# Download and setup the model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")
utterance = "I want to order a Pizza"
# Tokenize the utterance
inputs = tokenizer(utterance, return_tensors="pt")
# inputs
res = model.generate(**inputs)
# res
# Decoding the model output
tokenizer.decode(res[0])
# Decoding the inputs
tokenizer.decode(inputs['input_ids'][0])
import speech_recognition as sr  
def speechtoText():                                                                      
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        inp= r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    return inp
def generate_chat():
    counter=0
    while True:
        inp=speechtoText() 
        if inp in [" ","q"]:
            break
        inputs = tokenizer(inp, return_tensors="pt")#pt = pytorch if tensorflow make pt as tf
        res = model.generate(**inputs)
        aud=tokenizer.decode(res[0])
        res=''
        res+=aud[3:]
        res=res[:len(res)-4]
        print(res)
        aud = gTTS(text=res, lang="en", slow=False,tld='co.in')
        #date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        # test ="voice"+str(counter)+".wav"
        # test ="voice.wav"
        # counter+=1
        aud.save('voice.mp3')
        data, samplerate = sf.read("voice.mp3")
        sf.write("audio.wav", data, samplerate)
        # os.system("start {}".format(test))
        os.system('python3 test.py')
        # os.system("xdg-open {}".format(test))
        # duration = eyed3.load(test).info.time_secs
        # time.sleep(duration) 
    print("You left the chat.....")
generate_chat()