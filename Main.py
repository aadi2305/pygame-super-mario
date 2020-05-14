import pygame
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))

#title of game
pygame.display.set_caption("Super Mario")

#Setting Icon
icon = pygame.image.load("Images/Mario1.png")
pygame.display.set_icon(icon)

#loading all the images
bg1 = pygame.image.load("Images/BG1.png")
bg2 = bg1
mario1 = pygame.image.load("Images/Mario1.png")
mario2 = pygame.image.load("Images/Mario2.png")
mario3 = pygame.image.load("Images/Mario2.png")
walking_list = [mario1, mario2, mario3]

#all the fuctions and classes
def walking_mario():
	screen.blit(mario1, (200,400))
	screen.blit(mario2, (200,400))
	screen.blit(mario2, (200,400))

def show():
	global points
	screen.blit(bg1, (x_bg1, 0))
	screen.blit(bg1, (x_bg2, 0))
	if add == 0:
		screen.blit(mario1, (200, 400))
	if add!= 0:
		screen.blit(walking_list[points/3], (200,400))
		points +=1
		if points >=  9:
			points = 0
def bg_loop():
	global x_bg1
	global x_bg2
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



#all the variables
x_bg1 = 0
x_bg2 = 1280
add = 0
speed = 20
running = True
points = 0

#the game loop 
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
				
	
	
	bg_loop()
	show()
	


	pygame.display.update()
	clock.tick(30)