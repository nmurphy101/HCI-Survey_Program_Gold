#Package Imports
import pygame, sys
from pygame.locals import *

#Initilizer for pygame
pygame.init()

# With and Height of the app window
width = 400
height = 300

# Displaying the window
DISPLAYSURF = pygame.display.set_mode((0, 0), FULLSCREEN)

# Window Caption
pygame.display.set_caption('HCI Gold Group - Study')

# Main game loop
while True: 
	# Pygame event handler
	for event in pygame.event.get():
		
		# Player clicks the red "X" button on window
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	# Draw the screen		
	pygame.display.update()