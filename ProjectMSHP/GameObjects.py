"""В этом модуле хранятся классы игровых объектов."""
import pygame

class Player:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        """
        Initializing the game object.
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
        self.__speed: int = 2

        self.__speed_fall: int = 0
        self.__gravity: bool = True

        self.__direction: dict = {
            pygame.K_w: False, pygame.K_a: False,
            pygame.K_s: False, pygame.K_d: False
        }
        self.__diagonal_coefficient: float = 1 / (2 ** 0.5)

    def get_direction_keys(self) -> dict:
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

    def check_event(self, event) -> None:
        """
        Check buttons
        :event.type: True or False
        """

        if event.type == pygame.KEYDOWN:
            self.__direction[event.key] = True
        elif event.type == pygame.KEYUP:
            self.__direction[event.key] = False

    def check_logic(self, screen_width, screen_height) -> None:
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

        #Стены

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

    def check_collision(self, enemy) -> bool:
        """
        check collision enemy
        :param enemy: rect
        :return: bool
        """
        return self.__rect.colliderect(enemy.get_rect())
    def check_collision2(self, enemy2) -> bool:
        """
        check_collision enemy2
        :param enemy2: rect
        :return: bool
        """
        return self.__rect.colliderect(enemy2.get_rect())

    def move(self, acceleration_of_gravity: float) -> None:
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
    def draw(self, screen) -> None:
        """
        Draw player
        """
        # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)


class Enemy:
    def __init__(self, x: int, y: int, screen_width: int, screen_height: int) -> None:
        """
        Initializing the game object.
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
        self.__speed: int = 1
        self.__diagonal_coefficient: float = 1 / (2 ** 0.5)
    def get_rect(self):
        """
        get_rect
        :return: copy rect
        """
        return self.__rect.copy()
    def check_event(self, event) -> None:
        """
        None
        """
        pass

    def check_logic(self, screen_width, screen_height) -> None:
        """
        Wall collisions
        """
        if self.__rect.x < 60:
            self.__rect.x = 60
        elif self.__rect.x > screen_width - 100:
            self.__rect.x = screen_width - 100
        if self.__rect.y < 60:
            self.__rect.y = 60
        elif self.__rect.y > screen_height - 100:
            self.__rect.y = screen_height - 100

    def check_collision(self, enemy2) -> bool:
        """
        check_collision enemy2
        :return: True or False
        """
        return self.__rect.colliderect(enemy2.get_rect())
    def move(self, player) -> None:
        """
        Move
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

    def draw(self, screen) -> None:
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
    def __init__(self, screen_width: int, screen_height: int, x: int, y: int) -> None:
        """
        Initializing the game object.
        :param screen_width: int
        :param screen_height: int
        :param x: int
        :param y: int
        """
        # Размеры

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

    def check_event(self, event) -> None:
        pass

    def check_logic(self, screen_width, screen_height) -> None:
        pass

    def check_collision(self, player) -> None:
        return self.__rect.colliderect(player.get_rect())


    def move(self) -> None:
        pass

    def draw(self, screen) -> None:
        # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)
