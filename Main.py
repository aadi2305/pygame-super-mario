import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
bg1 = pygame.image.load("Images/BG1.png")
bg2 = bg1
mario = pygame.image.load("Images/Mario1.png")
x_bg1 = 0
x_bg2 = 1280
add = 0
speed = 20
running = True 
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running =False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				add = speed
			if event.key == pygame.K_RIGHT:
				add = -speed
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				add = 0
				
	x_bg1 = x_bg1 + add
	x_bg2 = x_bg2 + add
	if x_bg1 <= -1280:
		x_bg1 = 1280
	if x_bg2 <=-1280:
		x_bg2 = 1280
	if x_bg2 >1280:
		x_bg2 = -1280
	if x_bg1 >1280:
		x_bg1 = -1280
	

	screen.blit(bg1, (x_bg1,0))
	screen.blit(bg2, (x_bg2,0))
	screen.blit(mario, (200,400))


	pygame.display.update()