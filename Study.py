#Package Imports
import pygame, sys, tkinter as tk, math
from pygame.locals import *
from tkinter import messagebox
from pygame.locals import *
from random import *

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

# Function quit with a dialogue option
def quit():
	root = tk.Tk()
	root.withdraw()
	result = messagebox.askquestion("Warning","Do you want to quit?", icon="warning")
	if result == 'yes':
		pygame.time.set_timer ( pygame.USEREVENT , 0 )
		pygame.quit()
		sys.exit()

# Initilizer for pygame
pygame.init()
print("Pygame initilized")

# Frames per second setting
FPS = 30
fpsClock = pygame.time.Clock()

# With and Height of the app window
WIDTH = 1440
HEIGHT = 900

# Displaying the window
DISPLAYSURF = pygame.display.set_mode([WIDTH, HEIGHT])

# Window Caption
pygame.display.set_caption('HCI Gold Group - Study')

# Game Clock Timer Event
# Stop a timer with" pygame.time.set_timer ( pygame.USEREVENT , 0 ) "
pygame.time.set_timer(pygame.USEREVENT, 1000)
gameSeconds = 0

# A trial hasn't started yet, so data won't be recorded
inTrials = False
# Check for completion of the instructions 
instructionsComplete = False
# Check for completion of the tutorials and the time of completion
tutorialsComplete = False
tutorialsDoneTime = 0
# Number of trials completed
trialDoneCounter = 0
# Number of testing blocks completed 
blocksCompleted = 0
# Number of click errors
clickErrors = 0
# Starting check 
start = False
# Set up colors
WHITE = (255, 255, 255)

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
# Initiliztion of the trial block (1 block = 12 trials)
trialBlock = []
# The random function will give a predictible pattern each run
seed(50)

# Generate the first block of random trials
for trial in PossibleTrialsList:
	if randint(1,2) == 1: # Insert the trial at the end of the block if 1
		trialBlock.append(trial)
	else: # Insert the trial at the start of the block if 2
		trialBlock.insert(0,trial)
print("First block generated: " + str(trialBlock) )		
# The trail currently being performed
currentTrial = trialBlock.pop()
print("First trial: " + str(currentTrial))

# Main game loop
while True: 
	# Pygame event handler
	for event in pygame.event.get():
		
		# Player clicks the red "X" button on window
		if event.type == QUIT :
			print("red x quit")
			quit()
			
		# Add 1 to seconds to gameSeconds var every 1000ms	
		elif event.type == pygame.USEREVENT: 
			gameSeconds += 1
		
		# Display the instructions if they haven't been read yet
		if instructionsComplete == False and start == False:
			start = True
			print("instructions loaded")
			instructionsImg = pygame.image.load('instructions.png')
			DISPLAYSURF.blit(instructionsImg, [0, 0])
			print("after instructions loaded")
		
		# Key Press Down Event (ASCII Codes)
		if event.type == pygame.KEYDOWN:
			print("Keydown event activated")
			
			# If excape key was pressed quit the game
			if event.key == 27: 
				print("ESC Pressed")
				quit()	
				
			#Pressing space to complete the instructions and then tutorials to move on to the trials
			# If space bar is pressed
			if event.key == 32:
				print("Spacebar Pressed")
				print(str(gameSeconds))
				#Allow the player to complete the instructions 
				# if they haven't yet and 15 seconds or more have passed
				if instructionsComplete == False and gameSeconds >= 5:
					print("Instructions Completed")
					instructionsComplete == True
					# Clear the screen of the instructions
					DISPLAYSURF.fill( (0,0,0) )
					
				
				# Start doing trials (tutorial first)
				if instructionsComplete == True:
					print(str(instructionsComplete))
					print("In trials now and drew the first trial circle")
					# Now in trials
					inTrials = True
					
					print( str(int(WIDTH/2+(currentTrial[1]*currentTrial[2]))) )
					print( str(int(HEIGHT/2)) )
					print( str(currentTrial[0]) )
					print( str(currentTrial[2]) )
					# Draw the current trial circle (when space bar is pressed) 
					pygame.draw.circle(DISPLAYSURF, WHITE, [20, 20], 1000)
					# pygame.draw.circle(DISPLAYSURF, WHITE, [WIDTH//2+(currentTrial[1] * currentTrial[2]), HEIGHT//2], currentTrial[0], 0)
					
					# Current trial being completed
					trialDoneCounter += 1
					
					# if the tutorials haven't been done yet, and the player has completed 3 or more test trials 
					if trialDoneCounter >=3 and tutorialsComplete == False:
						print("Tutorials Completed" + str(tutorialsComplete))
						#mark the time that the tutorials were completed
						tutorialsDoneTime = gameSeconds
						# Mark the tutorials as completed
						tutorialsComplete == True
						# Reset the trial block so it gets regenerated for real trials
						trialBlock = []
						# Reset the number of trials completed as the previous ones are just tutorials
						trialDoneCounter = 0
						# Clear the screen of the last trial
						DISPLAYSURF.fill( (0,0,0) )
				
		# Mouse Press Down Event		
		elif event.type == pygame.MOUSEBUTTONDOWN and inTrials == True:
			print("Mouse Down Event Activated")
			# Set the position of the mouse as x and y when clicked
			x, y = event.pos
			
			click = DISPLAYSURF.get_at(pygame.mouse.get_pos()) == WHITE
			
			# Sucessful click on the circle object
			if click == 1:
				print("Click successful")
				##Do other stuff as well like print to a file about the trial info, errors, time completed, etc
				
				# Clear the surface of the completed trial circle
				DISPLAYSURF.fill( (0,0,0) )
				## Display a success message or make a success sound
				successImg = pygame.image.load('success.png')
				# Clear the surface of the success message
				DISPLAYSURF.fill( (0,0,0) )
				
				# If currently in a trial
				if inTrials == True:
					# Increase successful trial counter
					trialDoneCounter += 1

					# If test block is empty generate the next block
					if not trialBlock:
						# Increment the number of blocks completed
						blocksCompleted += 1
						
						# Generate the next block of random trials
						for trial in PossibleTrialsList:
							choice = randint(1,3) # Three random choices
							if choice == 1: # Insert the trial at the end of the block
								trialBlock.append(trial)
							elif choice == 2: # Insert the trial at the start of the block
								trialBlock.insert(0,trial)
							else: # Insert the trial at the middle of the block
								trialBlock.insert(len(trialBlock)/2,trial)
										
					# Pop the current test block stack to get the next trial
					currentTrial = trialBlock.pop()
					
			# Unsuccessful click on the circle object
			else:
				print("click unsuccessful")
				# If currently in a trial
				if inTrials == True:
					print("Click is trial misclick error")
					# Increase click error count 
					clickErrors += 1
				
		# Display section
		## Display number of trials completed vs needed to do yet (i.e. 2/120)
		## Code to do this ^ here	
		
		if blocksCompleted == 10:
			print("10 blocks completed")
			##Do other stuff as well like print maybe
			pygame.quit()
			sys.exit()
			
	# Draw/Update the screen		
	pygame.display.update()
	
	# Tick the fps clock
	fpsClock.tick(FPS)
	
	
	
	
	
	