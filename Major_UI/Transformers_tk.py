import tkinter as tk
import threading
import queue
import torch
import eyed3
import os
import time
from gtts import gTTS
import datetime
import soundfile as sf
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import speech_recognition as sr

# Download and setup the model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

class ChatWindow:
    def __init__(self, master):
        self.master = master
        master.title("Chat with Blenderbot")

        self.chat_history = tk.Text(master)
        self.chat_history.pack()

        self.speech_queue = queue.Queue()
        self.processing_thread = threading.Thread(target=self.process_speech)
        self.processing_thread.start()

        self.listen_button = tk.Button(master, text="Speak", command=self.listen)
        self.listen_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def listen(self):
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:
            print("Start Talking:")
            self.chat_history.insert(tk.END, "Start Talking:\n")
            self.chat_history.see(tk.END)
            self.master.update()
            audio = r.listen(source)
        self.speech_queue.put(r.recognize_google(audio))

    def process_speech(self):
        while True:
            speech = self.speech_queue.get()
            if speech == "q":
                break
            inputs = tokenizer(speech, return_tensors="pt")
            res = model.generate(**inputs)
            aud=tokenizer.decode(res[0])
            res=''
            res+=aud[3:]
            res=res[:len(res)-4]
            print(res)
            # self.chat_history.insert(tk.END, f"{res}\n")
            self.chat_history.insert(tk.END, f"model: {res}\n")
            self.chat_history.see(tk.END)
            self.master.update()
            aud = gTTS(text=res, lang="en", slow=False,tld='co.in')
            aud.save('voice.mp3')
            data, samplerate = sf.read("voice.mp3")
            sf.write("audio.wav", data, samplerate)
            # os.system('python3 textured_talking.py')
            os.system('python3 animation_check2.py')

def run_chat_window():
    root = tk.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()

if __name__ == "__main__":
    run_chat_window()
