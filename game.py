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
        self.centre = [self.X+30, self.Y+30]
        self.dX = 0
        self.dY = 0
        self.rect = self.image.get_rect(center=self.centre)


    # Link to rotation: https://gamedev.stackexchange.com/questions/132163/how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d
    def rotate(self):
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        rel_X, rel_Y = mouse_X - self.X-30, mouse_Y - self.Y-30
        angle = (180 / math.pi) * -math.atan2(rel_Y, rel_X) - 90
        self.image = pygame.transform.rotate(self.original_img, int(angle))
        self.rect = self.image.get_rect(center=self.centre)
        print(self.rect)
        print('Pos: ', mouse_X,mouse_Y)
        print('Angle: ', angle)
        
    
    def movement(self):
        pass
        
    
    def debug(self):
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0,0,0), self.centre, (mouse_X, mouse_Y), 2)


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
            if event.type == pygame.MOUSEMOTION:
                arrow.rotate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    arrow.dY = -0.3
                if event.key == pygame.K_s:
                    arrow.dY = 0.3
                if event.key == pygame.K_a:
                    arrow.dX = -0.3
                if event.key == pygame.K_d:
                    arrow.dX = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    arrow.dY = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    arrow.dX = 0
        
        arrow.centre[1] += arrow.dY
        arrow.centre[0] += arrow.dX
        arrow.load_player(arrow.rect.x, arrow.rect.y)
        arrow.debug()
    
        pygame.display.update()
    
    
if __name__ == '__main__':
    main()