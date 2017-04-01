#Package Imports
import pygame, sys
from pygame.locals import *

#########################################
##Example User Defined Event (Right before main game loop)
## def checkAllKeys ( a , b , c ):
##	if a == True and b == True and c == True:
##		ev = pygame.event.Event ( pygame.USEREVENT )
##       		pygame.event.post ( ev )
##------------------------------------------------------------------------------
##Example of event handling for user defined event (In main game loop)
##  elif event.type == pygame.USEREVENT:
##	print ( "You have pressed a, b, and c" )
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
# Stop a timer with" pygame.time.set_timer ( pygame.USEREVENT , 0 ) "
pygame.time.set_timer(pygame.USEREVENT, 1000)
gameSeconds = 0

# A trial hasn't started yet, so data won't be recorded
inTrials = False
# Check for completion of the instructions 
instructionsComplete = false
# Check for completion of the tutorials and the time of completion
tutorialsComplete = false
tutorialsDoneTime = 0
# Number of trials completed
trialDoneCounter = 0

# Trial possibility list that will be used to build random trial stacks
# Types: size-radius=(Small, Medium, Large), distance-to-center=(close, far),      direction=(Left, Right)
# Types: size-radius=(16px, 32px, 64px),          distance-to-center=(128px, 512px), direction=direction=(L, R)
Sm = 16
Me = 32
La =64
Cl = 128
Fa = 512
Le = -1
Ri = 1
# Organized list sorted by Size then direction then distance
PossibleTrialsList = [ [Sm,Cl,Le], [Sm,Fa,Le], [Sm,Cl,Ri], [Sm,Fa,Ri],   [Me,Cl,Le], [Me,Fa,Le], [Me,Cl,Ri], [Me,Fa,Ri],   [La,Cl,Le], [La,Fa,Le], [La,Cl,Ri], [La,Fa,Ri] ]

# The random function will give a predictible pattern each run
random.seed = 50


# Main game loop
while True: 
	# Pygame event handler
	for event in pygame.event.get():

		# Player clicks the red "X" button on window
		if event.type == QUIT :
			pygame.quit()
			sys.exit()
			
		# Add 1 to seconds to gameSeconds var every 1000ms	
		elif event.type == pygame.USEREVENT: 
			gameSeconds += 1
		
		# Key Press Down Event (ASCII Codes)
		elif event.type == pygame.KEYDOWN:
			# If excape key was pressed quit the game
			if event.key == ord ( "ESC" ): 
				pygame.time.set_timer ( pygame.USEREVENT , 0 )
				pygame.quit()
				sys.exit()	
				
			#Pressing space to complete the instructions and then tutorials to move on to the trials
			# Key Press Down Event on space
			if event.key == ord ( "space" );
				#Allow the player to complete the instructions 
				# if they haven't yet and 15 seconds or more have passed
				if instructionsComplete == false and gameSeconds >= 15:
					instructionsComplete == true
					
				# Allow the player to complete the tutorial and move to actual trials
				# if the instructions are complete, the tutorials haven't been yet, and the player has completed 3 or more test trials 
				if instructionsComplete == true and tutorialComplete == false and trialDoneCounter <=3:
					#mark the time that the tutorials were completed
					tutorialsDoneTime = gameSeconds
					# Zero out trials completed as the ones done thus far were pratice
					trialDoneCounter = 0
					tutorialComplete == true
					inTrials = true
				
				
		# Mouse Press Down Event		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# Set the position of the mouse as x and y when clicked
			x, y = event.pos
			
			##Need to create the object class being clicked (i.e. CircleObject)
			# Sucessful click on the circle object
			if clickobject.get_rect().collidepoint(x,y) == True:
				## Remove current trail circle objects
				## Display a success message or make a success sound
				## After a few game seconds display the next trial circle objects
				
				# If currently in a trial
				if inTrials == True:
					## Increase successful trial counter
					## 
					#Remove the code below with actual code
					tempNonsense = 0
		
					
			# Unsuccessful click on the circle object
			if clickobject.get_rect().collidepoint(x,y):	
				# If currently in a trial
				if inTrials == True:
					## Increase click error count var
					#Remove the code below with actual code
					tempNonsense = 0
		
		# Display section
		## Display number of trials completed vs needed to do yet (i.e. 2/120)
		## Code to do this ^ here	
		
	# Draw/Update the screen		
	pygame.display.update()
	
	
	
	
	
	
	