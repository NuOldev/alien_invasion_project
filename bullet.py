import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        # Acceso a la Clase principal y a las caracteristicas y caracteristicas de la pantalla.
        self.screen = ai_game.screen
        # Acceso a la Clase principal y al modulo Settings
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crear bala en (0,0) por defecto
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # el rect.midtop de la bala ahora coincide con el rect.midtop de la nave.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Usando float para un movimiento más preciso de las balas.
        self.y = float(self.rect.y)

    def update(self):
        """Moviendo la bala hacia arriba."""
        # Se resta pues el eje (y) hacia abajo suma y hacia arriba resta.
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y  # se actualiza el rect.y con el decremento self.y

    def draw_bullet(self):
        """Dibuja la bala en la pantalla."""
        # Dibuja un rectangulo en (self.screen) con el color (self.color) y el rectangulo es (self.rect = el rectangulo de la bala)
        pygame.draw.rect(self.screen, self.color, self.rect)
