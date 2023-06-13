from pyrr import Matrix44, Vector3
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class ObjLoader:
    def __init__(self):
        self.vertices = []
        self.normals = []
        self.indices = []

    def load_model(self, file_path):
        self.vertices = []
        self.normals = []
        self.indices = []

        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("v "):
                    vertex = list(map(float, line.split()[1:4]))
                    self.vertices.append(vertex)
                elif line.startswith("vn "):
                    normal = list(map(float, line.split()[1:4]))
                    self.normals.append(normal)
                elif line.startswith("f "):
                    face = list(map(lambda x: int(x.split("/")[0]) - 1, line.split()[1:4]))
                    self.indices.extend(face)

    def render(self):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glLoadIdentity()
        
        # Set the camera position and orientation
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
        
        # Set the projection matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 800/600, 0.1, 50.0)  # Adjust the frustum values here
        
        # Set the modelview matrix
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Render the model
        glBegin(GL_TRIANGLES)
        for i in range(0, len(self.indices), 3):
            face = self.indices[i:i+3]
            glNormal3fv(self.normals[face[0]])
            glVertex3fv(self.vertices[face[0]])
            glNormal3fv(self.normals[face[1]])
            glVertex3fv(self.vertices[face[1]])
            glNormal3fv(self.normals[face[2]])
            glVertex3fv(self.vertices[face[2]])

        glEnd()

        pygame.display.flip()


# Create a Pygame window
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Create an instance of ObjLoader and load the model
obj_loader = ObjLoader()
obj_loader.load_model("model.obj")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Render the model
    obj_loader.render()
