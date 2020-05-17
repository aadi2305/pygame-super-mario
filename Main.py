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

sl_mario1 = pygame.image.load("Images/New Marios/flipsmallmario1.png")
sl_mario2 = pygame.image.load("Images/New Marios/flipsmallmario2.png")
sl_mario3 = pygame.image.load("Images/New Marios/flipsmallmario3.png")
sl_mario4 = pygame.image.load("Images/New Marios/flipsmallmario4.png")
sl_jump = pygame.image.load("Images/New Marios/flipsmalljump.png")
walking_sleft = [sl_mario1, sl_mario2, sl_mario3, sl_mario4, sl_jump]

gl_mario1 = pygame.image.load("Images/New Marios/flipgreenmario1.png")
gl_mario2 = pygame.image.load("Images/New Marios/flipgreenmario2.png")
gl_mario3 = pygame.image.load("Images/New Marios/flipgreenmario3.png")
gl_mario4 = pygame.image.load("Images/New Marios/flipgreenmario4.png")
gl_jump = pygame.image.load("Images/New Marios/flipgreenmariojump.png")
walking_gleft = [gl_mario1, gl_mario2, gl_mario3, gl_mario4, gl_jump]
walking_left = [walking_sleft, walking_gleft]

sr_mario1 = pygame.image.load("Images/New Marios/smallmario1.png")
sr_mario2 = pygame.image.load("Images/New Marios/smallmario2.png")
sr_mario3 = pygame.image.load("Images/New Marios/smallmario3.png")
sr_mario4 = pygame.image.load("Images/New Marios/smallmario4.png")
sr_jump = pygame.image.load("Images/New Marios/smalljump.png")
walking_sright = [sr_mario1, sr_mario2, sr_mario3, sr_mario4, sr_jump]

gr_mario1 = pygame.image.load("Images/New Marios/greenmario1.png")
gr_mario2 = pygame.image.load("Images/New Marios/greenmario2.png")
gr_mario3 = pygame.image.load("Images/New Marios/greenmario3.png")
gr_mario4 = pygame.image.load("Images/New Marios/greenmario4.png")
gr_jump = pygame.image.load("Images/New Marios/greenmariojump.png")
walking_gright = [gr_mario1, gr_mario2,gr_mario3, gr_mario4, gr_jump]

walking_right = [walking_sright, walking_gright]
star_box = pygame.image.load("Images/Star box.png")
wall3block = pygame.image.load("Images/3wallblock.png")

power = 1
#all the funtions
def jump():
	global x_mario, y_mario, jumpPoints, isJump, d
	if isJump == True:
		if jumpPoints[power] >=0:
			neg = 1
		elif jumpPoints[power] <0:
			neg = -1
		y_mario = y_mario - ((jumpPoints[power]**2)*0.25*neg)
		if y_mario > 425:
			y_mario = 425
		jumpPoints[power]-=1
		if jumpPoints[power] < -jumpHeight:
			jumpPoints[power] = jumpHeight
			isJump = False
			y_mario = 425

def mario_walking():
	global points, x_mario,y_mario
	if x_mario <= 960 and x_mario >= 180:
		x_mario -= mario_add
	if x_mario == 980:
		x_mario = 960
	if x_mario == 160:
		x_mario = 180
	if isJump == True:
		jump()
		if right == False and left == False:
			if temprf == False:
				screen.blit(walking_right[power][4], (x_mario, y_mario))
			if temprf == True:
				screen.blit(walking_left[power][4], (x_mario, y_mario))
		if right:
			screen.blit(walking_right[power][4], (x_mario,y_mario))
		if left:
			screen.blit(walking_left[power][4], (x_mario,y_mario))
	if isJump == False:
		if right == False and left == False:
			if temprf == False:
				screen.blit(walking_right[power][0], (x_mario, y_mario))
			if temprf == True:
				screen.blit(walking_left[power][0], (x_mario, y_mario))
		if right:
			if  bg_add !=0 or mario_add!=0:
				screen.blit(walking_right[power][points/5], (x_mario,y_mario))
				points +=1
				if points >=  20:
					points = 0
		if left:
			if bg_add !=0 or mario_add!=0:
				screen.blit(walking_left[power][points/5], (x_mario,y_mario))
				points +=1
				if points >=  20:
					points = 0

def blitByXpos(img, xPos, yPos):
	if xPos<1300:
		screen.blit(img,(xPos, yPos))
	else:
		pass

def bg_loop():
	global x_bg1
	global x_bg2 , x_bg3
	if x_mario >= 960 or x_mario <= 180:
		
		x_bg1 = x_bg1 + bg_add
		x_bg2 = x_bg2 + bg_add
		x_bg3 = x_bg3 + bg_add
	if x_bg1 <= -1280:
		x_bg1 = 1280*2
	if x_bg2 <=-1280:
		x_bg2 = 1280*2
	if x_bg3 <=-1280:
		x_bg3 = 1280*2

	if x_bg1 >1280*2:
		x_bg1 = -1280
	if x_bg2 >1280*2:
		x_bg2 = -1280
	if x_bg3 >1280*2:
		x_bg3 = -1280

def show():
	#screen.fill((77,195,255))
	screen.blit(bg1, (x_bg1, 0))
	screen.blit(bg1, (x_bg2, 0))
	screen.blit(bg1, (x_bg3, 0))
	mario_walking()
	blitByXpos(starbox1.pngImage, starbox1.x_pos, starbox1.y_pos)
	blitByXpos(wall3block_e.pngImage, wall3block_e.x_pos, wall3block_e.y_pos)
	pygame.display.update()

def collision(xPos, yPos, img):
	global isJump
	global x_mario,y_mario
	width,height = img.get_rect().size

	if y_mario + mario_height <=yPos:
		if x_mario < xPos or x_mario+ mario_width > xPos +width:
			isJump = True
	if x_mario >= xPos and x_mario <= xPos +width:
		if y_mario + mario_height <= yPos+height:
			y_mario = yPos- mario_height
			isJump = False
		elif y_mario <= yPos+height and y_mario>= yPos:
			y_mario = yPos+height
			x_mario = xPos

	if x_mario + mario_width >= xPos and x_mario+ mario_width <= xPos +width:
		if y_mario + mario_height <= yPos:
			y_mario = yPos- mario_height
			isJump = False

		elif y_mario <= yPos + height and y_mario>= yPos:
			y_mario = yPos+height
			x_mario= xPos - mario_width
	

class Elements():
	def __init__(self, x_pos, y_pos, pngImage):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.pngImage = pngImage
	def x_movement(self):
		if x_mario >= 960 or x_mario <= 180:
			pass

#all the variables
x_bg1 = 0
x_bg2 = 1280
x_bg3 = 1280*2
x_mario = 200
y_mario = 425
bg_add = 0
mario_add = 0
speed = 20
running = True
points = 0
isJump = False
right = False
left = False
temprf = 0
jumpPoints = [11, 14]
jumpHeight = jumpPoints[power]
mario_width, mario_height = sr_mario1.get_rect().size

#all the elements
starbox1 = Elements(1280+135, 280, star_box)
wall3block_e = Elements(1280+135+150, 280, wall3block)
#the game loop 
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running =False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				mario_add = speed
				bg_add = speed
				right = False
				left = True
				temprf = True
			if event.key == pygame.K_RIGHT:
				mario_add = -speed
				bg_add = -speed
				right = True
				left= False
				temprf = False
			if event.key == pygame.K_UP:
				isJump = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				bg_add = 0
				mario_add = 0
				right = False
				left= False
	if x_mario >= 960 or x_mario <= 180:
		starbox1.x_pos += bg_add
		wall3block_e.x_pos += bg_add

	collision(starbox1.x_pos, starbox1.y_pos, star_box)
	collision(wall3block_e.x_pos, wall3block_e.y_pos, wall3block)
	bg_loop()
	show()




	
	clock.tick(25)