import pyvista as pv
import atexit
from playsound import playsound

# Load the 3D model
mesh = pv.read("avatar.obj")

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

# Start the audio playback
# playsound(audio_file, block=False)

# Define a function to be called when the program exits
def cleanup():
    if audio_file is not None:
        playsound(audio_file)
    if playsound._playsoundWin is not None:
        playsound._playsoundWin.kill()


# Register the cleanup function with the atexit module
atexit.register(cleanup)

# Start the visualization with automatic exit after audio is done
plotter.show(interactive=False)
