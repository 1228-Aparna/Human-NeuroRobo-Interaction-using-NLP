import cv2
import threading
from pydub import AudioSegment
from pydub.playback import play

# Load the video file
video_path = './lipsync.mp4'
cap = cv2.VideoCapture(video_path)

# Load the audio file
audio_path = './audio.wav'
audio = AudioSegment.from_wav(audio_path)

# Create a flag to indicate when the video playback is finished
video_finished = False

# Define a function to play the audio in a separate thread
def play_audio():
    play(audio)
    # Set the flag to indicate that the audio playback is finished
    global video_finished
    video_finished = True

# Start audio playback in a separate thread
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

# Adjust video frame rate and delay for slower playback
frame_rate = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)//2

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        # Reset the video capture if it reaches the end
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Display the frame
    cv2.imshow('Video', frame)

    # Introduce a delay for slower playback
    cv2.waitKey(delay)

    # Exit the loop if the 'q' key is pressed or both video and audio playback are finished
    if cv2.waitKey(1) & 0xFF == ord('q') or video_finished:
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
