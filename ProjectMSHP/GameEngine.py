"""Модуль, отвечающий за работу с PyGame."""
import pygame
from GameObjects import Player, Enemy, Enemy2, Brick
class Game:
    def __init__(self, width: int =800, height: int =600, fps: int =60) -> None:
        """
        Initializing the game object.
        """
        pygame.init()

        self.__width : int = width
        self.__height : int = height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg_sprite = pygame.transform.smoothscale(
            pygame.image.load("Images/bg.jpg").convert(),
            (self.__width, self.__height))
        self.__bg_gameover = pygame.transform.smoothscale(
            pygame.image.load("Images/gameover.jpg").convert(),
            (self.__width, self.__height))
        self.__fps: int = fps
        self.__clock = pygame.time.Clock()
        self.__game_end: bool = False

        self.__acceleration_of_gravity: float = 9.8 / self.__fps

        self.__player = Player(self.__width, self.__height)
        self.__enemy = Enemy(200, 250, self.__width, self.__height)
        self.__enemy2 = Enemy2(152, 445, self.__width, self.__height)
        self.__brick1 = Brick(self.__width, self.__height,353, 442)
        self.__brick2 = Brick(self.__width, self.__height, 353, 387)
        self.__brick3 = Brick(self.__width, self.__height, 353, 332)
        self.__brick4 = Brick(self.__width, self.__height, 403, 332)
        self.__brick5 = Brick(self.__width, self.__height, 453, 332)
        self.__brick6 = Brick(self.__width, self.__height, 453, 387)
        self.__brick7 = Brick(self.__width, self.__height, 453, 442)

        self.__brick8 = Brick(self.__width, self.__height, 203, 113)
        self.__brick9 = Brick(self.__width, self.__height, 203, 168)
        self.__brick10 = Brick(self.__width, self.__height, 253, 168)
        self.__brick11 = Brick(self.__width, self.__height, 303, 168)
        self.__brick12 = Brick(self.__width, self.__height, 303, 168)
        self.__brick13 = Brick(self.__width, self.__height, 303, 113)

        self.font_comicsans = pygame.font.SysFont("comicsansms",35)
        self.__txt_color: tuple[int, int, int] = (255, 0, 0)
        #self.__steps_for_win = 1000  # Сколько кадров до победы
        self.__curent_steps: int = 0  # Сколько кадров сейчас

    def __del__(self) -> None:
        """
        Clearing memory at the end of work.
        """
        pygame.quit()

    def run(self) -> None:
        """
        Starting the game's game loop.
        """
        while not self.__game_end:
            self.__check_events()
            self.__move_objects()
            self.__check_logic()

            self.__draw()

            self.__curent_steps += 1
            self.__clock.tick(self.__fps)

    def __check_events(self) -> None:
        """
        Checking events that occurred since the previous frame.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True

            self.__player.check_event(event)

            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and \
                    event.key in self.__player.get_direction_keys():
                self.__player.check_event(event)

    def __check_logic(self) -> None:
        """
        Processing game logic.
        """
        self.__player.check_logic(self.__width, self.__height)
        '''
        if self.__curent_steps >= self.__steps_for_win:
            print("Победа!")
            #self.__bg_sprite = self.__bg_gameover
            self.__game_end = True
        '''

        if self.__player.check_collision(self.__enemy) or self.__player.check_collision2(self.__enemy2):
            print("Вы столкнулись с Плохишишем!")
            print(f"Вы набрали - {self.__curent_steps}")
            self.__bg_sprite = self.__bg_gameover

            self.__game_end: bool = True

    def __move_objects(self) -> None:
        """
        Gravitation and enemy moving
        """
        self.__player.move(self.__acceleration_of_gravity)
        self.__enemy.move(self.__player)
    def __draw(self) -> None:
        """
        Draw all objects
        """
        self.__screen.blit(self.__bg_sprite, (0, 0))
        self.__player.draw(self.__screen)
        self.__enemy.draw(self.__screen)
        self.__enemy2.draw(self.__screen)
        self.__brick1.draw(self.__screen)
        self.__brick2.draw(self.__screen)
        self.__brick3.draw(self.__screen)
        self.__brick4.draw(self.__screen)
        self.__brick5.draw(self.__screen)
        self.__brick6.draw(self.__screen)
        self.__brick7.draw(self.__screen)
        self.__brick8.draw(self.__screen)
        self.__brick9.draw(self.__screen)
        self.__brick10.draw(self.__screen)
        self.__brick11.draw(self.__screen)
        self.__brick12.draw(self.__screen)
        self.__brick13.draw(self.__screen)

        text_img = self.font_comicsans.render(f"Score: {self.__curent_steps}",True,self.__txt_color)
        self.__screen.blit(text_img,(10,10))
        pygame.display.flip()
        self.__x, self.__y = pygame.mouse.get_pos()
        #print(self.__x, self.__y)


