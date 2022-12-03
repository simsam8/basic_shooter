import pygame
import math



class Player:
    def __init__(self, screen) -> None:
        self.original_img = pygame.image.load('./imgs/arrow.png')
        self.image = self.original_img.copy()
        self.X = 300
        self.Y = 300
        self.centre = [self.X+30, self.Y+30]
        self.dX = 0
        self.dY = 0
        self.rect = self.image.get_rect(center=self.centre)
        self.screen = screen


    # Link to rotation: https://gamedev.stackexchange.com/questions/132163/how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d
    def rotate(self):
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        rel_X, rel_Y = mouse_X - self.centre[0], mouse_Y - self.centre[1]
        angle = (180 / math.pi) * -math.atan2(rel_Y, rel_X) - 90
        self.image = pygame.transform.rotate(self.original_img, int(angle))
        self.rect = self.image.get_rect(center=self.centre)
        #print(self.rect)
        #print('Pos: ', mouse_X,mouse_Y)
        #print('Angle: ', angle)
        
    
    def move(self, amount, direction):
        '''
        H for horisontal
        L for lateral
        '''
        if direction == "H":
            self.dX = amount
        if direction == "L":
            self.dY = amount
        #self.centre[0] += self.dX
        #self.centre[1] += self.dY
        
    # Show debugging
    def debug(self):
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        pygame.draw.line(self.screen, (0,0,0), self.centre, (mouse_X, mouse_Y), 2)


    # Draw player to scrren
    def load_player(self, x,y):
        self.rotate() # better way to implement?
        self.rect = self.image.get_rect(center=self.centre)
        self.screen.blit(self.image, (x,y))