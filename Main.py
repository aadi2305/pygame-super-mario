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
bg1 = pygame.image.load("Images/BG1.png").convert()
bg2 = bg1

sl_mario1 = pygame.image.load("Images/small_mario/flipsmallmario1.png")
sl_mario2 = pygame.image.load("Images/small_mario/flipsmallmario2.png")
sl_mario3 = pygame.image.load("Images/small_mario/flipsmallmario3.png")
walking_sleft = [sl_mario1, sl_mario2, sl_mario3]

sr_mario1 = pygame.image.load("Images/small_mario/smallmario1.png")
sr_mario2 = pygame.image.load("Images/small_mario/smallmario2.png")
sr_mario3 = pygame.image.load("Images/small_mario/smallmario3.png")
walking_sright = [sr_mario1, sr_mario2, sr_mario3]

#all the funtions
def mario_walking():
	global points
	if right == False and left == False:
		if temprf == False:
			screen.blit(sr_mario1, (200, 425))
		if temprf == True:
			screen.blit(sl_mario1, (200, 425))
	if right:
		if add!= 0:
			screen.blit(walking_sright[points/3], (200,425))
			points +=1
			if points >=  9:
				points = 0
	if left:
		if add!= 0:
			screen.blit(walking_sleft[points/3], (200,425))
			points +=1
			if points >=  9:
				points = 0

def show():
	
	screen.blit(bg1, (x_bg1, 0))
	screen.blit(bg1, (x_bg2, 0))
	mario_walking()
	

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
def jump():
	pass


#all the variables
x_bg1 = 0
x_bg2 = 1280
add = 0
speed = 20
running = True
points = 0

right = False
left = False
temprf = 0

#the game loop 
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running =False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				add = speed
				right = False
				left = True
				temprf = True
			if event.key == pygame.K_RIGHT:
				add = -speed
				right = True
				left= False
				temprf = False

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				add = 0
				right = False
				left= False
				
	
	
	bg_loop()
	show()
	


	pygame.display.update()
	clock.tick(60)