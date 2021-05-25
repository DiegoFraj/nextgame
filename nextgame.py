# Import libraries
import sys, pygame, pygame.freetype, random
from pygame.locals import *

# Set size of window
size = 1200,800
background_img = pygame.image.load('notebook.jpg')
#background_img = pygame.transform.scale(background_img, (1280, 768))

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


class PORTRAIT:

    def __init__(self, next_scene):
        # Initialize variables
        self.background = pygame.Surface(size)

        '''
        self.flechaImg = pygame.image.load('flecha.png')
        self.flechaImg_rect = self.flechaImg.get_rect()
        self.flechaImg_rect = self.flechaImg_rect.move(1000,500)
        '''

        self.next_scene = next_scene
        
    def draw(self,screen, dt):
        # Draw them 
        font = pygame.font.SysFont("comicsansms",80)
        img = font.render('Tareas',True, NAVYBLUE)
        screen.blit(img, (500,334)) 
        #screen.blit(self.flechaImg, (1000,500))
    
    def update(self, events, dt):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.flechaImg_rect.collidepoint(mouse_pos):
                    #pygame.time.set_timer(fade_event, 1000)
                    return (self.next_scene, None)

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
    #fondoImg = pygame.image.load('notebook.jpg')

    # Setting up Scenes
    dt = 0
    scenes = {
        'PORTADA': PORTRAIT('SEGUNDA'),

    }
    scene = scenes['PORTADA']

    # Start running game loop
    run=True
    while run:
        
        # Background img
        screen.blit(background_img, (0,0))

        # EVENTS 
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: # Si el evento es salir de la ventana, terminamos
                run = False
        
        scene.draw(screen, dt)
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == '__main__':
    main()