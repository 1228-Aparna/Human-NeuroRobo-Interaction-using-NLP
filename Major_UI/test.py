import pyvista as pv
import cv2
import numpy as np
from scipy.io import wavfile
import os

# Load the 3D model with shape keys
mesh = pv.read("model.obj")

# Load the texture file
texture = pv.read_texture("texture.png")

# Add the texture to the mesh
mesh.textures["my_texture"] = texture

# Set the texture map of the mesh to the texture name
mesh.texture_map = "my_texture"

# Create a plotter and add the mesh
plotter = pv.Plotter()
plotter.add_mesh(mesh)

# Set the camera position
plotter.camera_position = [(0, 0, 2), (0, 0, 0), (0, 1, 0)]

# Load the audio file
audio_file = "audio.wav"
rate, audio = wavfile.read(audio_file)

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 25.0, (1280, 720))

# Calculate the time intervals for each frame
duration = len(audio) / rate
n_frames = int(duration * 25)  # assuming 25 fps
frame_intervals = np.linspace(0, duration, n_frames + 1)

# Define the shape keys and their corresponding phonemes
shape_keys = {
    "mouth_wide": ["E", "I", "O"],
    "mouth_narrow": ["U", "OO"],
    "mouth_smile": ["AH"],
}

# Define the shape key weights for each phoneme
shape_key_weights = {
    "mouth_wide": 0,
    "mouth_narrow": 0,
    "mouth_smile": 0,
}

# Iterate over each frame and calculate the shape key weights
for i in range(n_frames):
    ti = frame_intervals[i]
    audio_frame = audio[int(ti * rate) : int((ti + 1 / 25) * rate)]
    shape_key_weights = calculate_shape_key(ti, audio_frame, shape_keys)

    # Apply the shape key weights to the mesh
    for key, value in shape_key_weights.items():
        mesh[key] = value

    # Render the frame and save to video
    plotter.write_frame()
    img = plotter.screenshot(transparent_background=True)
    out.write(cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGR))

# Release the video writer and close the plotter
out.release()
plotter.close()
