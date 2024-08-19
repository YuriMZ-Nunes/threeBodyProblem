import ctypes
import pygame
import sys
import platform

system = platform.system()

if system == "Windows":
    dll_name = "libthreebodyproblem.dll"
elif system == "Darwin":
    dll_name = "libthreebodyproblem.dylib"
else:
    dll_name = "libthreebodyproblem.so"

# DLL config
dll = ctypes.CDLL(f'./{dll_name}')

class Vector2D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]

dll.iteratePhysic.argtypes = [ctypes.c_int]
dll.iteratePhysic.restype = Vector2D

dll.addObject.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
dll.addObject.restype = None

# pygame config
pygame.init()

width, height = 1500, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Problema dos 3 corpos")
clock = pygame.time.Clock()

circles = [
    {'color': (255, 255, 255), 'pos': [475.0, 700.0], 'vel': [6, 0], 'strength': 1000, 'radius': 20, 'history': [], 'lineColor': (255, 0, 0)},
    {'color': (255, 255, 255), 'pos': [750.0, 300.0], 'vel': [-6, 6], 'strength': 1000, 'radius': 20, 'history': [], 'lineColor': (0, 255, 0)},
    {'color': (255, 255, 255), 'pos': [1025.0, 700.0], 'vel': [0, -6], 'strength': 1000, 'radius': 20, 'history': [], 'lineColor': (0, 0, 255)}
]

simulationPositions = []

def initObjects():
    for circle in circles:
        dll.addObject(circle['pos'][0], circle['pos'][1], circle['vel'][0], circle['vel'][1], circle['strength'])

def runSimulation(j):
    position = dll.iteratePhysic(j)
    simulationPositions.append([position.x, position.y])

def updateCirclesPosition():
    for circle in circles:
        if simulationPositions:
            position = simulationPositions.pop(0)
            circle['history'].append(position)
            if len(circle['history']) > 1000:
                circle['history'].pop(0)
            circle['pos'] = position

def draw():
    screen.fill((0, 0, 0))
    for circle in circles:
        if len(circle['history']) > 1:
            pygame.draw.lines(screen, circle['lineColor'], False, circle['history'], 2)
        pygame.draw.circle(screen, circle['color'], (int(circle['pos'][0]), int(circle['pos'][1])), circle['radius'])
    pygame.display.flip()


# begin

initObjects()

for _ in range(10000):
    for j in range(3):
        runSimulation(j)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    updateCirclesPosition()
    draw()

    clock.tick(60)

