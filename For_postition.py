import pygame
import random
import math
pygame.init()


screen = pygame.display.set_mode((1270,725))
pygame.display.set_caption("Super Mario")

background = pygame.image.load("Images/BG.png")
pipe = pygame.image.load("Images/circle.png")


pipeX = 500
pipeY = 0
Y_change = 0
X_change = 0
#game Loop
running = True
while running:
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				Y_change = -2
			if event.key == pygame.K_DOWN:
				Y_change =   2
			if event.key == pygame.K_LEFT:
				X_change =  -2
			if event.key == pygame.K_RIGHT:
				X_change =  2 

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				
					X_change =  0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				
					Y_change =  0


				

	print(pipeX, pipeY)
	pipeX += X_change
	pipeY += Y_change
	screen.blit(pipe,(pipeX, pipeY))
		



	




	
	
	pygame.display.update()