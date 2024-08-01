import pygame
from math import sqrt
from typing import Union


# Игрок
class Player:
    def __init__(self, screen_width, screen_height):
        """
        Construction
        """
        # Размеры

        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load("Images/shish.png").convert_alpha(),
            (screen_width // 18, screen_height // 13)
        )
        self.__rect = self.__sprite.get_rect()
        # Положение
        self.__rect.x = screen_width // 2 - self.__rect.width // 2 - 67
        self.__rect.y = screen_height // 2 - self.__rect.height // 2 - 87
        # Движение 
        self.__speed = 2

        self.__speed_fall = 0
        self.__gravity = True

        self.__direction = {
            pygame.K_w: False, pygame.K_a: False,
            pygame.K_s: False, pygame.K_d: False
        }
        self.__diagonal_coefficient = 1 / (2 ** 0.5)

    def get_direction_keys(self):
        """
        get_direction_keys
        :return: Dictionary
        """
        return self.__direction.keys()

    def get_rect(self):
        """
        get_rect
        :return: copy of self rect
        """
        return self.__rect.copy()

    def check_event(self, event):
        """
        Check buttons
        :event.type: True or False
        """

        if event.type == pygame.KEYDOWN:
            self.__direction[event.key] = True
        elif event.type == pygame.KEYUP:
            self.__direction[event.key] = False

    def check_logic(self, screen_width, screen_height):
        """
        Walls collisions
        :param screen_width: int
        :param screen_height: int
        :return: int
        """
        if self.__rect.x < 60:
            self.__rect.x = 60
        elif self.__rect.x > screen_width - 100:
            self.__rect.x = screen_width - 100
        if self.__rect.y < 60:
            self.__rect.y = 60
        elif self.__rect.y > screen_height - 110:
            self.__rect.y = screen_height - 110

        # Стены

        if 166 < self.__rect.x < 348 and 210 < self.__rect.y < 215:
            self.__rect.y = 215
        if 203 < self.__rect.x < 350 and self.__rect.y < 210:
            self.__rect.x = 350
        if 160 < self.__rect.x < 170 and self.__rect.y < 210:
            self.__rect.x = 160

        if 319 < self.__rect.x < 497 and 280 < self.__rect.y < 300:
            self.__rect.y = 280
            self.__speed_fall = 0
            self.__gravity = False
        if 319 < self.__rect.x < 497 and self.__rect.y > 301:
            self.__rect.x = 497
        if 305 < self.__rect.x < 310 and self.__rect.y > 301:
            self.__rect.x = 305

    def check_collision(self, enemy):
        """
        check collision enemy
        :param enemy: rect
        :return: bool
        """
        return self.__rect.colliderect(enemy.get_rect())

    def check_collision2(self, enemy2):
        """
        check_collision enemy2
        :param enemy2: rect
        :return: bool
        """
        return self.__rect.colliderect(enemy2.get_rect())

    def move(self, acceleration_of_gravity):
        """
        Move player
        :param acceleration_of_gravity: float
        """

        self.__rect.x += self.__speed * (self.__direction[pygame.K_d]
                                         - self.__direction[pygame.K_a])
        self.__rect.y += self.__speed * (self.__direction[pygame.K_s]
                                         - self.__direction[pygame.K_w])
        if self.__gravity:
            self.__speed_fall += acceleration_of_gravity
            self.__rect.y += self.__speed_fall

    def draw(self, screen):
        """
        Draw player
        """
        # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)


class Enemy:
    def __init__(self, x, y, screen_width, screen_height):
        """
        Construction
        :param x: int
        :param y: int
        :param screen_width: int
        :param screen_height: int
        """
        # Размеры

        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load("Images/badshish.png").convert_alpha(),
            (screen_width // 18, screen_height // 13)
        )
        self.__rect = self.__sprite.get_rect()
        # Положение
        self.__rect.x = x
        self.__rect.y = y
        # Движение
        self.__speed = 1
        self.__diagonal_coefficient = 1 / (2 ** 0.5)

    def get_rect(self):
        """
        get_rect
        :return: copy rect
        """
        return self.__rect.copy()

    def check_event(self, event):
        """
        None
        """
        pass

    def check_logic(self, screen_width, screen_height):
        """
        Wall collosions
        """
        if self.__rect.x < 60:
            self.__rect.x = 60
        elif self.__rect.x > screen_width - 100:
            self.__rect.x = screen_width - 100
        if self.__rect.y < 60:
            self.__rect.y = 60
        elif self.__rect.y > screen_height - 100:
            self.__rect.y = screen_height - 100

    def check_collision(self, enemy2):
        """
        check_collision enemy2
        :return: True or False
        """
        return self.__rect.colliderect(enemy2.get_rect())

    def move(self, player):
        """
        Move enemy
        """
        player_rect = player.get_rect()

        if self.__rect.x <= player_rect.x:
            self.__rect.x += self.__speed
        elif self.__rect.x >= player_rect.x + player_rect.width:
            self.__rect.x -= self.__speed
        if self.__rect.y <= player_rect.y:
            self.__rect.y += self.__speed
        elif self.__rect.y >= player_rect.y + player_rect.height:
            self.__rect.y -= self.__speed

        if 166 < self.__rect.x < 348 and 210 < self.__rect.y < 215:
            self.__rect.y = 215
        if 203 < self.__rect.x < 350 and self.__rect.y < 210:
            self.__rect.x = 350
        if 160 < self.__rect.x < 170 and self.__rect.y < 210:
            self.__rect.x = 160

        if 319 < self.__rect.x < 497 and 280 < self.__rect.y < 300:
            self.__rect.y = 280
        if 319 < self.__rect.x < 497 and self.__rect.y > 301:
            self.__rect.x = 497
        if 305 < self.__rect.x < 310 and self.__rect.y > 301:
            self.__rect.x = 305

    def draw(self, screen):
        """
        Draw Enemy
        :param screen: rect
        """
        # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)


class Enemy2(Enemy):
    def move(self, player):
        """
        Nothing important
        """

        while self.__rect.x != 0:
            self.__rect.x -= self.__speed


class Brick:
    def __init__(self, screen_width, screen_height, x, y):
        """
        Construction
        :param screen_width: int
        :param screen_height: int
        :param x: int
        :param y: int
        """
        # Размеры

        self.__direction = None
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load("Images/brick.jpg").convert_alpha(),
            (screen_width // 18, screen_height // 13)
        )
        self.__rect = self.__sprite.get_rect()
        # Положение
        self.__rect.x = x
        self.__rect.y = y

    # Получение клавиш управления
    def get_direction_keys(self):
        """
        Get control buttons
        :return: dictinary
        """
        return self.__direction.keys()

    def get_rect(self):
        """
        get rect
        :return: copy any rect
        """
        return self.__rect.copy()

    def check_event(self, event):
        pass

    def check_logic(self, screen_width, screen_height):
        pass

    def check_collision(self, player):
        return self.__rect.colliderect(player.get_rect())

    def move(self):
        pass

    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)


class Game:
    def __init__(self, width=800, height=600, fps=60):
        """
        Construction
        """
        pygame.init()

        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg_sprite = pygame.transform.smoothscale(
            pygame.image.load("Images/bg.jpg").convert(),
            (self.__width, self.__height))
        self.__bg_gameover = pygame.transform.smoothscale(
            pygame.image.load("Images/gameover.jpg").convert(),
            (self.__width, self.__height))
        self.__fps = fps
        self.__clock = pygame.time.Clock()
        self.__game_end = False

        self.__acceleration_of_gravity = 9.8 / self.__fps

        self.__player = Player(self.__width, self.__height)
        self.__enemy = Enemy(200, 250, self.__width, self.__height)
        self.__enemy2 = Enemy2(152, 445, self.__width, self.__height)
        self.__brick1 = Brick(self.__width, self.__height, 353, 442)
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

        self.font_comicsans = pygame.font.SysFont("comicsansms", 35)
        self.__txt_color = (255, 0, 0)
        # self.__steps_for_win = 1000  # Сколько кадров до победы
        self.__curent_steps = 0  # Сколько кадров сейчас

    def __del__(self):
        """
        Destruction
        :return: End of the game
        """
        pygame.quit()

    def run(self):
        """
        run all of class Game's functions
        """
        while not self.__game_end:
            self.__check_events()
            self.__move_objects()
            self.__check_logic()

            self.__draw()

            self.__curent_steps += 1
            self.__clock.tick(self.__fps)

    def __check_events(self):
        """
        Check exit of the game
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True

            self.__player.check_event(event)

            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and \
                    event.key in self.__player.get_direction_keys():
                self.__player.check_event(event)

    def __check_logic(self):
        """
        Check exit of the game
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

            self.__game_end = True

    def __move_objects(self):
        """
        Gravitation and enemy moving
        """
        self.__player.move(self.__acceleration_of_gravity)
        self.__enemy.move(self.__player)

    def __draw(self):
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

        text_img = self.font_comicsans.render(f"Score: {self.__curent_steps}", True, self.__txt_color)
        self.__screen.blit(text_img, (10, 10))
        pygame.display.flip()
        self.__x, self.__y = pygame.mouse.get_pos()
        # print(self.__x, self.__y)


def main():
    """
    Main code
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
