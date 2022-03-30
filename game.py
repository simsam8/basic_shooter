from tkinter import CENTER
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600,600))
#background = pygame.image.load('./imgs/space.jpg')

class Player:
    def __init__(self) -> None:
        self.original_img = pygame.image.load('./imgs/arrow.png')
        self.image = self.original_img.copy()
        self.X = 300
        self.Y = 300
        self.centre = (self.X-30, self.Y-30)
        self.dX = 0
        self.dY = 0


    # Link to rotation: https://gamedev.stackexchange.com/questions/132163/how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d
    def rotate(self):
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        rel_X, rel_Y = mouse_X - self.X-30, mouse_Y - self.Y-30
        angle = (180 / math.pi) * -math.atan2(rel_Y, rel_X)
        self.image = pygame.transform.rotate(self.original_img, int(angle))
        self.rect = self.image.get_rect(center=self.centre)
        print('Pos: ', mouse_X,mouse_Y)
        print('Angle: ', angle)


    def load_player(self, x,y):
        screen.blit(self.image, (x,y))


def main():
    
    arrow = Player()
    
    running = True
    while running:
        screen.fill((255,255,255))
        #screen.blit(background, (0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                arrow.rotate()
        
        arrow.load_player(arrow.X, arrow.Y)
    
        pygame.display.update()
    
    
if __name__ == '__main__':
    main()