"""
01 - Creando la clase Ship
02 - Creando el acceso a la clase AlienInvasion
03 - Descargando la imagen de la nave.
04 - Obteniendo su rectangulo
05 - Posicionamiento del rectangulo de la nave 
06 - Agregando metodo para dibujar la nave en su posicion dentro de la pantalla
"""

import pygame


class Ship:  # 01
    """A class to manage the ship."""

    def __init__(self, ai_game):  # 02
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # 03
        self.rect = self.image.get_rect()  # 04

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom  # 05

    def blitme(self):  # 06
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
