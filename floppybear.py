import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400,300))
print screen.get_rect()
pygame.display.set_caption("Floppy Bear - STumbles")

done = False

class Log_Top():
	def __init__(self, height, speed):
		self.width, self.height = 20, height
		self.left, self.top = 379,0
		self.color = [255,255,53]
		self.speed = speed
		self.log = pygame.Rect([self.left , self.top] , [self.width , self.height])
	def draw(self, screen):
		self.log = pygame.Rect([self.left , self.top] , [self.width , self.height])
		pygame.draw.rect(screen, self.color, self.log)
	def move(self):
		self.left -= self.speed
	def floor_collision(self):
		return self.log.colliderect(screen.get_rect())

class Log():
	def __init__(self, height, speed):
		self.width, self.height = 20, height
		self.left, self.top = 379,300-self.height
		self.color = [255,255,53]
		self.speed = speed
		self.log = pygame.Rect([self.left , self.top] , [self.width , self.height])
	def draw(self, screen):
		self.log = pygame.Rect([self.left , self.top] , [self.width , self.height])
		pygame.draw.rect(screen, self.color, self.log)
	def move(self):
		self.left -= self.speed
	def floor_collision(self):
		return self.log.colliderect(screen.get_rect())


class Bear():
	def __init__(self):
		self.gravity = 5
		self.left, self.top = 100, 100
		self.width, self.height = 20, 20
		self.color = [139,69,19]
		self.bear = pygame.Rect([self.left , self.top] , [self.width , self.height])
	def draw(self, screen):
		self.bear = pygame.Rect([self.left , self.top] , [self.width , self.height])
		pygame.draw.rect(screen, self.color, self.bear)
	def floor_collision(self):
		return self.bear.colliderect(screen.get_rect())
	def log_collision(self, log):
		return self.bear.colliderect(log)
	def flying(self):
		if self.floor_collision(): #when bear is flying
			self.top += self.gravity
			return True
		if not self.floor_collision(): #when bear is on floor
			return False

bear = Bear()
logs = []
log_tops = []
log_release = 8
clock = pygame.time.Clock()

while not done:
	screen.fill([50, 200, 50])
	keys = pygame.key.get_pressed()
	if pygame.event.get(pygame.QUIT): done = True #quits


	if bear.flying():
		if keys[K_UP]: bear.top -= 14
	if not bear.flying():
		done = True


	if not pygame.time.get_ticks() % log_release:
		r_height_top = random.randrange(90,130,3)
		r_height_bot = 300 - 112 - r_height_top
		logs.append(Log(r_height_bot, 5))
		log_tops.append(Log_Top(r_height_top, 5))
		r_height_top, r_height_bot = None, None

	for log in logs:
		if not bear.log_collision(log.log):
			log.move()
			log.draw(screen)
		if bear.log_collision(log.log):
			done = True
		if not log.floor_collision():
			logs.pop(0)
		try:
		# try to print logs[0].log (leftmost log)
			print(logs[0].log)
		except IndexError:
		# if there is no log on the screen just pass
			pass

	for top_log in log_tops:
		if not bear.log_collision(top_log.log):
			top_log.move()
			top_log.draw(screen)
		if bear.log_collision(top_log.log):
			done = True
		if not top_log.floor_collision():
			log_tops.pop(0)
		try:
		# try to print logs[0].log (leftmost log)
			print(log_tops[0].log)
		except IndexError:
		# if there is no log on the screen just pass
			pass

	bear.draw(screen)
	print pygame.time.get_ticks()
	clock.tick(42)
	pygame.display.flip()

print "Game Over - bear touched log"
print "final score is %d" % (pygame.time.get_ticks())
