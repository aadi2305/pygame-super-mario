'''def show():
	screen.fill((77,195,255))
	screen.blit(bg1, (x_bg1, 0))
	screen.blit(bg1, (x_bg2, 0))
	screen.blit(bg1, (x_bg3, 0))
	mario_walking()
	pygame.display.update()

def bg_loop():
	global x_bg1
	global x_bg2 , x_bg3
	if x_mario >= 960 or x_mario <= 180:
		x_bg1 = x_bg1 + bg_add
		x_bg2 = x_bg2 + bg_add
		x_bg3 = x_bg3 + bg_add
	if x_bg1 < -1280:
		x_bg1 = 1280*2
	if x_bg2 <-1280:
		x_bg2 = 1280*2
	if x_bg3 <-1280:
		x_bg3 = 1280*2
	if x_bg2 >1280*2:
		x_bg2 = -1280
	if x_bg1 >1280*2:
		x_bg1 = -1280
	if x_bg3 >1280*2:
		x_bg3 = -1280
def jump():
	global x_mario, y_mario, jumpPoints, isJump, d
	if isJump == True:
		if jumpPoints >=0:
			neg = 1
		elif jumpPoints <0:
			neg = -1
		y_mario = y_mario - ((jumpPoints**2)*neg)
		jumpPoints-=1
		if jumpPoints < -jumpHeight:
			jumpPoints = jumpHeight
			isJump = False'''