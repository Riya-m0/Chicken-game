import pygame
import random

screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background = pygame.image.load("background.jpg")
user = pygame.image.load("Nobita1.png")
heart = pygame.image.load("heart.png")


def dis_score(score):
  font = pygame.font.SysFont("Comic Sans MS", 35)
  text = "Score: "+str(score)
  txt_image = font.render(text,True,(0,255,0))
  screen.blit(txt_image,[10,10])


alive=True
clock = pygame.time.Clock()

def random_offset():
 return -1*random.randint(100,1800)
heart_y = [random_offset(),random_offset(),random_offset(),random_offset()]
#chic_y = [random_offset()]
user_x = 150
score = 0

def crash(idx):
 global score
 global alive
 global  done
 score = score - 20
 print("crashed with ", idx, score)
 heart_y[idx] = random_offset()
 if score < -60 :
  alive =False



def update_heart_pos(idx):
 global score
 if heart_y[idx]>600:
  heart_y[idx]=random_offset()
  score = score + 5
  print("score",score)
 else:
  heart_y[idx] = heart_y[idx]+5


while alive:
 pygame.event.get()
 keys = pygame.key.get_pressed()
 if keys[pygame.K_RIGHT] and user_x<280:
  user_x = user_x + 8
 elif keys[pygame.K_LEFT] and user_x>0:
  user_x = user_x - 8
 update_heart_pos(0)
 update_heart_pos(1)
 update_heart_pos(2)
 update_heart_pos(3)

 screen.blit(background,[0,0])
 screen.blit(user, [user_x,520])
 screen.blit(heart, [0,heart_y[0]])
 screen.blit(heart, [150, heart_y[1]])
 screen.blit(heart, [200, heart_y[2]])
 screen.blit(heart,[300,heart_y[3]])
 if heart_y[0]>500 and user_x<70:
  crash(0)

 if heart_y[2] >500  and user_x<200:
  crash(2)

 if heart_y[1]>500 and user_x >100 and user_x<200:
  crash(1)

 if heart_y[3] >500  and user_x>200:
  crash(3)


 dis_score(score)

 pygame.display.update()
 clock.tick(75)