import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra zaliczeniowa: Ping-Pong")

BLACK = (0, 0, 0)
WHITE = (255,255,255)
LINE = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL = 5
P_WIDTH, P_HEIGHT = 40, 100

P1_IMAGE = pygame.image.load(os.path.join('Assets', 'P1.png'))
P1 = pygame.transform.scale(P1_IMAGE, (P_WIDTH,P_HEIGHT))

P2_IMAGE = pygame.image.load(os.path.join('Assets', 'P2.png'))
P2 = pygame.transform.scale(P2_IMAGE, (P_WIDTH,P_HEIGHT))

def draw_window(P1_position, P2_position):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, LINE)
    WIN.blit(P1, (P1_position.x, P1_position.y))
    WIN.blit(P2, (P2_position.x, P2_position.y))
    pygame.display.update()
    
def P1_move(keys_pressed, P1_position):
    if keys_pressed[pygame.K_s] and P1_position.y + VEL + P_HEIGHT < HEIGHT:
        P1_position.y += VEL
    if keys_pressed[pygame.K_w] and P1_position.y - VEL > 0:
        P1_position.y -= VEL

def P2_move(keys_pressed, P2_position):
    if keys_pressed[pygame.K_DOWN] and P2_position.y + VEL + P_HEIGHT < HEIGHT:
        P2_position.y += VEL
    if keys_pressed[pygame.K_UP] and P2_position.y - VEL > 0 :
        P2_position.y -= VEL
 
def main():
    P1_position = pygame.Rect(100, 300, P_WIDTH, P_HEIGHT)
    P2_position = pygame.Rect(760, 300, P_WIDTH, P_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        P1_move(keys_pressed, P1_position)
        P2_move(keys_pressed, P2_position)
        draw_window(P1_position, P2_position)
    pygame.quit()

if __name__ == "__main__":
    main()
            
