import tkinter as tk
from PIL import Image, ImageTk
import os
root = tk.Tk()
root.geometry("1024x786")
root.title("Human-NeuroRobo Interaction")

def Talk_to_me():
    os.system('python3 Transformers_tk.py')

def guess():
    os.system('python3 ob_detection_tk.py')

def mimic():
    os.system('open mimic.mp4')

# set background color to blue
root.configure(bg="#0099cc")

header_label = tk.Label(root, text="Welcome back, Friend", font=("Helvetica", 24), fg="white", bg="#0099cc")
header_label.pack(pady=40)
# create image object
image = Image.open("model.png")
# create a Tkinter PhotoImage object from the image
bg_image = ImageTk.PhotoImage(image)

# create a Canvas widget and add the background image
canvas = tk.Canvas(root, width=490, height=512, highlightthickness=0)
canvas.create_image(0, 0, anchor='nw', image=bg_image)
canvas.place(relx=0.5, rely=0.5, anchor='center')

# create buttons
button1 = tk.Button(root, text="Talk to me !", font=("Helvetica", 16), fg="white", bg="#006699", padx=20, pady=10,command = Talk_to_me)
button2 = tk.Button(root, text="Let me Guess...", font=("Helvetica", 16), fg="white", bg="#006699", padx=20, pady=10, command = guess)
button3 = tk.Button(root, text="I am a Mimic !", font=("Helvetica", 16), fg="white", bg="#006699", padx=20, pady=10, command = mimic)

# place buttons in a row with space between them at the bottom of the page
button1.place(relx=0.3, rely=0.9, anchor='center')
button2.place(relx=0.5, rely=0.9, anchor='center')
button3.place(relx=0.7, rely=0.9, anchor='center')

# start the main event loop
root.mainloop()
