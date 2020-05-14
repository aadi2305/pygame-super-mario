import pygame
import random
import math
pygame.init()


screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Super Mario")

background1 = pygame.image.load("Images/BG1.png")
background2 = background1
pipe = pygame.image.load("Images/pipe.png")

x_bg1 = 0
bg_change = 0
x_bg2 = 1280
#game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				bg_change =   6
			if event.key == pygame.K_LEFT:
				bg_change =  -6
			

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				bg_change =  0
			
	
	x_bg1 += -2
	x_bg2 = x_bg2 + 1280
	screen.blit(background1, (x_bg1,0))
	screen.blit(background2, (x_bg2,0))
	#screen.blit(pipe, (500,0))
	if x_bg1 == -1280:
		x_bh1 = 1280

	pygame.display.update()