from random import randint
import time 
import pygame
import time
pygame.init()


'''створюємо вікно програми'''

back = (200,255,255)#колір фону (background)
mw = pygame.display.set_mode((1000,800))#Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

'''клас прямокутник'''

class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)#прямокутник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)

    def outline(self, frame_color, thickness):#обведення існуючого прямокутника
        pygame.draw.rect(mw, frame_color,self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


'''клас напис'''

class Label(Area):
    def set_text(self, text, fsize =12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, ( self.rect.x + shift_x , self.rect.y + shift_y ) )

YELLOW = (255,255,0)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
DARK_BLUE = (0,0,100)
BLUE = (80,80,255)
LIGHT_RED = (250, 128, 114)
LIGHT_BLUE = (80, 80, 255)
WHITE = (200,255,255)

cards = []
num_cards = 4



x = 70

text_time = Label(0,0,50,50,back)
text_time.set_text ('time:', 25, (250, 128, 114))
text_time.draw (20,20)


timer = Label (33,50,50,50,back)
timer.set_text ('0', 25, (250, 128, 114))
timer.draw (0,0)

score = Label(400,0,50,50,back)
score.set_text ('score:', 25, (250, 128, 114))
score.draw (20,20)


score2 = Label(439,50,50,50,back)
score2.set_text ('0', 25, (250, 128, 114))
score2.draw (0,0)



for i in range(num_cards):
    new_card = Label(x,170,70,100, YELLOW)
    new_card.outline(BLUE,10)
    new_card.set_text('CLICK',25)
    cards.append(new_card)
    x = x + 100

a = 20

sc = 0

cur_time = time.time()

start_time = time.time()

while True:
    if a == 20:
        a = 0
        randnum = randint (0,3)
        for i in range (4):
            cards[i].color(YELLOW)
            if i == randnum:
                cards[i].draw(10,40)
            else:
                cards[i].fill()
    else:
        a += 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            for i in range (4):
                if cards[i].collidepoint(x,y):
                    if i == randnum:
                        cards[i].color(GREEN)
                        sc += 1
                    else:
                        cards[i].color(RED)
                        sc -= 1 
                    cards[i].fill()
        score2.set_text(str (sc), 25, (250, 128, 114))
        score2.draw(0,0)
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
            


    new_time = time.time()
    if new_time - start_time >= 10:
        timer = None
        text_lose = Label(0,0,500,500,WHITE)
        text_lose.set_text("Lose!" , 120, RED)
        text_lose.draw(250,250)
        
        
    
    if sc >=5:
        timer = None
        text_lose = Label(0,0,500,500,WHITE)
        text_lose.set_text("win!" , 120,GREEN)
        text_lose.draw(250,250)
        



    pygame.display.update()
    clock.tick(40)