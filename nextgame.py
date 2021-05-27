# Import libraries
import sys, pygame, pygame.freetype, random
from pygame.locals import *

# Set size of window
size = 1200,800

# Colours    R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (127,   0, 255)
CYAN     = (  0, 255, 255)

fade_event = pygame.USEREVENT + 1
fade_timer = 10

class PORTRAIT:

    def __init__(self, next_scene):
        # Initialize variables
        self.background = pygame.Surface(size)
        
        self.flechaImg = pygame.image.load('flecha.png')
        self.flechaImg = pygame.transform.scale(self.flechaImg, (200,200))
        self.flechaImg_rect = self.flechaImg.get_rect()
        self.flechaImg_rect = self.flechaImg_rect.move(800,500)

        self.next_scene = next_scene
        
    def draw(self,screen, dt):
        # Draw them 
        font = pygame.font.SysFont("comicsansms",80)
        img = font.render('Tareas',True, BLACK)
        screen.blit(img, (500,334)) 
        screen.blit(self.flechaImg, (800,500))
    
    def update(self, events, dt):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.flechaImg_rect.collidepoint(mouse_pos):
                    pygame.time.set_timer(fade_event, 1000)
                    return (self.next_scene, None)

class GAME1:
    def __init__(self, next_scene):
        self.background = pygame.Surface(size)

        # For fade effect
        self.fade = False
        self.fade_time = 0
        self.current_alpha = 255
        self.part = 1
        
        self.g1 = (200,460)
        self.g2 = (420,460)
        self.g3 = (640,460)
        self.g4 = (860,460)

        # Load and rect all images
        self.girl1 = pygame.image.load('girl1.png')
        self.girl1 = pygame.transform.scale(self.girl1, (200,200))
        self.girl1_rect = self.girl1.get_rect()
        self.girl1_rect = self.girl1_rect.move(self.g3)

        self.girl2 = pygame.image.load('girl2.png')
        self.girl2 = pygame.transform.scale(self.girl2, (200,200))
        self.girl2_rect = self.girl2.get_rect()
        self.girl2_rect = self.girl2_rect.move(self.g4)

        self.girl3 = pygame.image.load('girl3.png')
        self.girl3 = pygame.transform.scale(self.girl3, (200,200))
        self.girl3_rect = self.girl3.get_rect()
        self.girl3_rect = self.girl3_rect.move(self.g1)

        self.girl4 = pygame.image.load('girl4.png')
        self.girl4 = pygame.transform.scale(self.girl4, (200,200))
        self.girl4_rect = self.girl4.get_rect()
        self.girl4_rect = self.girl4_rect.move(self.g2)



        self.question = pygame.image.load('question.png')
        self.question = pygame.transform.scale(self.question, (200,200))
        self.question_rect = self.question.get_rect()
        self.question_rect = self.question_rect.move(830,200)

        '''
        self.imagenes1_array = ['girl1.png','girl2.png','girl3.png','girl4.png']
        self.rects = []

        for i in self.imagenes1_array:
            i2 = pygame.image.load(i)
            i2 = pygame.transform.scale(i2, (200,200))
            s = pygame.Surface(i2.get_size())
            r = s.get_rect()
            
            r.x = (200)
            r.y = (200)
            margin = 5
            rl = [rect.inflate(margin*2, margin*2) for rect in self.rects]
            if len(self.rects) == 0:
                self.rects.append(r)
                r.x = r.x + 210
        '''

    def start(self, gamestate):
        self.gamestate = gamestate

    def draw(self,screen, dt):
        self.background = pygame.Surface(size)

        font = pygame.font.SysFont("comicsansms",50)
        text1 = font.render('Laura se levanta por la mañana...',True, BLACK)

         # First half     
        if self.part == 1 and not self.fade:
            # Show image to remember and then fade out
            screen.blit(text1, (250, 360))
    
        elif self.part == 1 and self.fade:
            self.fade_time += dt
            if self.fade_time > fade_timer:
                self.fade_time = 0
                text1.set_alpha(self.current_alpha)
               
                self.current_alpha -= 3
                if self.current_alpha == 0:
                   self.fade = False
                   self.part = 2
            # Blit the fade effect
            screen.blit(text1, (250, 360))
        
        else:
            # Second half 
            text2 = font.render('¿Qué es lo siguiente que hará Laura?',True, BLACK)
            screen.blit(text2, (200,100))

            screen.blit(self.girl1, (200, 200))
            screen.blit(self.girl2, (420, 200))
            screen.blit(self.girl3, (640, 200))
            screen.blit(self.question, (860, 200))

            screen.blit(self.girl3, (self.g1))
            screen.blit(self.girl4, (self.g2))
            screen.blit(self.girl2, (self.g3))
            screen.blit(self.girl1, (self.g4))

    def update(self, events, dt):
       for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN: 
                mouse = event.pos
                if self.girl1_rect.collidepoint(mouse)|self.girl2_rect.collidepoint(mouse)|self.girl3_rect.collidepoint(mouse):
                    print('not ok')
                elif self.girl4_rect.collidepoint(mouse):
                    print('ok')


def main():
    # Inicializamos pygame
    pygame.init()
    
    # Definimos las dimensiones de la ventana (1600 x 900px) y reloj
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Ponemos el título e icono y fondo de la ventana
    pygame.display.set_caption("Tareas")
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    fondoImg = pygame.image.load('notebook.jpg')

    # Setting up Scenes
    dt = 0
    scenes = {
        'PORTADA': PORTRAIT('SEGUNDA'),
        'SEGUNDA': GAME1('SEGUNDA'),

    }
    scene = scenes['PORTADA']

    # Start running game loop
    run=True
    while run:
        
        # Background img
        screen.blit(fondoImg, (0,0))

        # EVENTS 
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: # Si el evento es salir de la ventana, terminamos
                run = False
            if event.type == fade_event:
                scene.fade = True
                pygame.time.set_timer(fade_event, 0)
                print("fade event")

        result = scene.update(events, dt)
        if result:
            next_scene, state = result
            if next_scene:
                scene = scenes[next_scene]
                scene.start(state)

        scene.draw(screen, dt)
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == '__main__':
    main()