"""
Accediendo al módulo bullet
Agrupando las balas que sean disparadas
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Clase general para manejar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Iniciar el juego y crear sus recursos."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # Contenedor de las balas.

    def run_game(self):
        """Iniciar el loop principal del juego."""

        while True:
            self._check_events()
            self.ship.update()
            # Llama a update() dentro del módulo bullet por cada elemento/bala que se encuentre en el grupo.
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Flags to True
    def _check_keydown_events(self, event):
        """Responding for keypress."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  # Si se presiona Space...
            self._fire_bullet()  # Corre _fire_bullet()

    # Flags to False
    def _check_keyup_events(self, event):
        """Responding for keyreleases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        new_bullet = Bullet(self)  # Instancia de Bullet...
        self.bullets.add(new_bullet)  # Añade una bala al contenedor...


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
