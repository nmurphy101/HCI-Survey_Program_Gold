#Package Imports
import pygame, sys
from pygame.locals import *

#########################################
#Example User Defined Event (Right before main game loop)
# def checkAllKeys ( a , b , c ):
#	if a == True and b == True and c == True:
#		ev = pygame.event.Event ( pygame.USEREVENT )
#       		pygame.event.post ( ev )
#------------------------------------------------------------------------------
#Example of event handling for user defined event (In main game loop)
#  elif event.type == pygame.USEREVENT:
#	print ( "You have pressed a, b, and c" )
#########################################

#Initilizer for pygame
pygame.init()

# With and Height of the app window
width = 400
height = 300

# Displaying the window
DISPLAYSURF = pygame.display.set_mode((0, 0), FULLSCREEN)

# Window Caption
pygame.display.set_caption('HCI Gold Group - Study')

# Game Clock Timer Event
# Stop a timer with" pygame.time.set_timer ( pygame.NAMEHERE , 0 ) "
pygame.time.set_timer(pygame.GAMECLOCK, 1000)
gameSeconds = 0

######################################
# Trial Clock Timer Event (THIS GOES WHERE TRIALS START)
# pygame.time.set_timer(pygame.TRIALCLOCK, 1000)
# trialSeconds = 0
######################################

# A trial hasn't started yet, so data won't be recorded
trial = False

# Main game loop
while True: 
	# Pygame event handler
	for event in pygame.event.get():
		
		# Player clicks the red "X" button on window
		if event.type == QUIT :
			pygame.quit()
			sys.exit()
			
		# Add 1 to seconds var every 1000ms	
		elif event.type == pygame.GAMECLOCK: 
			seconds += 1
		
		# Key Press Down Event (ASCII Codes)
		elif event.type == pygame.KEYDOWN:
			# If excape key was pressed quit the game
			if event.key == ord ( "ESC" ): 
				pygame.time.set_timer ( pygame.GAMECLOCK , 0 )
				pygame.quit()
				sys.exit()	
				
		# Mouse Press Down Event		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# Set the position of the mouse as x and y when clicked
			x, y = event.pos
			#Need to create the object being clicked
			if clickobject.get_rect().collidepoint(x,y) and trial == True:
				# 
			if not clickobject.get_rect().collidepoint(x,y) trial == True:	
			
	# Draw/Update the screen		
	pygame.display.update()
	
	
	
	
	
	
	