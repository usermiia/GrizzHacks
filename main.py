import pygame
import time
from random import randrange
#Attribution: pythonprogramming.net, github.com

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Grizz Hacks")

# Tables
table1 = pygame.transform.scale(pygame.image.load("table2.png"), (200, 200))
table2 = pygame.transform.scale(pygame.image.load("table3.png"), (200, 200))
tables = [table1, table2]


o1 = pygame.transform.scale(pygame.image.load("monster.png"), (100, 100))
o2 = pygame.transform.scale(pygame.image.load("pizzaMonster.png"), (100, 100))
o3 = pygame.transform.scale(pygame.image.load("sodaMonster.png"), (100, 100))

obstacles = [o1, o2, o3]


# Build Character
def character(x, y):
    character = pygame.transform.scale(pygame.image.load("forward1.png"), (200, 200))
    window.blit(character, (x, y))
    
ran1 = randrange(300)
ran2 = randrange(300)
ran3 = randrange(300)
ran4 = randrange(300)
ran5 = randrange(300)
ran6 = randrange(300)

pizzas = 10

tips = 0


clock = pygame.time.Clock()

# Character display 
x = 50
y = 300
width = 40
height = 60
astx=100
asty=100
destx=300
desty=0
dest2x=0
dest2y=100
pizzaToDeliver=10
oldPizza=10
tips=0.00
times=0
times1=0
tips=0



# Jumping
isJump = False
jumpCount = 10


def background():
  window.fill((181, 101, 29))


  # Target
  destination = pygame.transform.scale(table1, (200, 200))
  window.blit(destination,(destx, desty))
  window.blit(destination,(dest2x,dest2y))

  # Obstacle
  window.blit(o1, (astx,asty))

def collisiontesthorizontal(x,astx):
    if x>astx+60 and x<astx+100:
      return True
    else:
      return False
def collisiontestvertical(y,desty):
    if y>desty and y<desty+100:
      return True
    else:
      return False  

#Collision Tests and Incrementing Points
    if collisiontesthorizontal(x,astx):
      if pizzaToDeliver<10:
          pizzaToDeliver+=1
          #print(pizzaToDeliver)
      pass
    if collisiontestvertical(y,desty) and collisiontesthorizontal(y,desty):
        if keys[pygame.K_SPACE]:
          if times<1:
            pizzaToDeliver-=1
            tips+=0.05
            #print(pizzaToDeliver)
            milliseconds=clock.tick()
            print(milliseconds)
            seconds=milliseconds/100
            if seconds>=20:
              tips-=0.02
            print(tips)
            times+=1
    if collisiontestvertical(y,desty) and collisiontesthorizontal(y,desty):
        if keys[pygame.K_SPACE]:
          if times1<1:
            pizzaToDeliver-=1
            tips+=0.05
            #print(pizzaToDeliver)
            milliseconds=clock.tick()
            print(milliseconds)
            seconds=milliseconds/100
            if seconds>=5:
              tips-=0.02
            print(tips)
            times1+=1
          else: 
            tips+=0
    if times1==1 and times==1:
      times1=0
      times=0

run = True
while run:
  clock.tick(27)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  background()

  # Movement
  keys = pygame.key.get_pressed()


  
  if keys[pygame.K_RIGHT]:
    x += 10

  if keys[pygame.K_LEFT]:
    x -= 10

  if keys[pygame.K_UP]:
    y -= 10


  if keys[pygame.K_DOWN]:
    y += 10

  if pizzas <= 10:
    if (x-30) < ran1 and (x+30) > ran1 and (y+30) > ran2 and (y-30) <ran2:
      ran1 = randrange(300)
      ran2 = randrange(300)
      pizzas -= 1

      tips += .5

    if (x-30) < ran3 and (x+30) > ran3 and (y+30) > ran4 and (y-30) <ran4:
      ran3 = randrange(300)
      ran4 = randrange(300)
      pizzas -= 1

      tips += .5
    
  window.blit(tables[1], (ran1, ran2))
  window.blit(tables[0], (ran3, ran4))

  window.blit(obstacles[0], (ran5, ran2))
  window.blit(obstacles[2], (ran1, ran6))
  


    
  character(x, y)
 


 



  pygame.display.update()

  def endScreen():
    global pause, tips, pizza, obstacles
    pause = 0
    pizza = 0
    obstacles = []

    largeFont = pygame.font.SysFont('comicsans', 80)
    currenttips = largeFont.render('Total tips:'+str(tips), 1, (255,255,255))
    pygame.display.update()

    tips = 0 

  def redrawWindow():
    #font
    largeFont = pygame.font.SysFont('comicsans', 30)
    text = largeFont.render('tips'+str(tips), 1, (255,255,255))
  

pygame.quit

