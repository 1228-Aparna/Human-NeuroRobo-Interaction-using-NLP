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

# Define a function to be called when the program exits
def cleanup():
    if audio_file is not None:
        playsound(audio_file)
    if playsound._playsoundWin is not None:
        playsound._playsoundWin.kill()


# Register the cleanup function with the atexit module
atexit.register(cleanup)

# Start the visualization
plotter.show(auto_close=False)

# Load the phoneme sequence
phonemes = ['aa', 'p', 't', 'k', 's', 'sil', 'sil', 'sil', 'aa', 'p', 't', 'k', 's', 'sil', 'sil', 'sil']

# Create a dictionary of facial expressions for each phoneme
facial_expressions = {
    'aa': {'mouth_open': 0.5, 'jaw_drop': 0.3},
    'p': {'lip_purse': 0.5, 'cheek_puff': 0.3},
    't': {'tongue_press': 0.5, 'lip_purse': 0.3},
    'k': {'jaw_drop': 0.5, 'tongue_press': 0.3},
    's': {'lip_stretch': 0.5, 'cheek_puff': 0.3},
    'sil': {}
}

# Loop through the phoneme sequence and update the facial expressions accordingly
for phoneme in phonemes:
    if phoneme in facial_expressions:
        mesh.clear_scalar_bar()
        mesh.set_scalars(facial_expressions[phoneme])
        plotter.update()
