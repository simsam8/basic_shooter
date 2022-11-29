import pygame
import math
from player import Player






class Game:
    
    FPS = 60
    PLAYER_MOVEMENT_SPEED = 5
    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        #self.background = pygame.image.load('./imgs/space.jpg')
        
        self.clock = pygame.time.Clock()
        
        
    def display_fps(self):
        font = pygame.font.SysFont("Arial", 18, bold=True)
        fps = str(int(self.clock.get_fps()))
        fps_display = font.render(fps, 1, (255,0,0))
        self.screen.blit(fps_display, (0,0))
        
    def run_game(self):
        arrow = Player(self.screen)
    
        running = True
        
        while running:
            self.screen.fill((255,255,255))
            #screen.blit(background, (0,0))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    arrow.rotate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        arrow.move(-game.PLAYER_MOVEMENT_SPEED, "L")
                    if event.key == pygame.K_s:
                        arrow.move(game.PLAYER_MOVEMENT_SPEED, "L")
                    if event.key == pygame.K_a:
                        arrow.move(-game.PLAYER_MOVEMENT_SPEED, "H")
                    if event.key == pygame.K_d:
                        arrow.move(game.PLAYER_MOVEMENT_SPEED, "H")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        arrow.dY = 0
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        arrow.dX = 0
            
            arrow.centre[1] += arrow.dY
            arrow.centre[0] += arrow.dX
            arrow.load_player(arrow.rect.x, arrow.rect.y)
            arrow.debug()

            game.display_fps()
            pygame.display.update()
            
            game.clock.tick(game.FPS)


    
    
if __name__ == '__main__':
    game = Game()
    game.run_game()