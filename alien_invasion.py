"""
* Refactoring
Nota: A un método con un guión bajo antes del nombre de este, se le
llama (helper method), estos funcionan dentro de la clase pero no están 
destinados para el uso fuera de la función.
01 - Creando helper method _check_events().
02 - Creando helper method _update_screen().
03 - Moviendo el codigo correspondiente a _check_events().
04 - Moviendo el codigo correspondiente a _update_screen().
05 - Simplificando el método principal run_game().
"""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Clase general para manejar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Iniciar el juego y crear sus recursos."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Create a pygame window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Iniciar el loop principal del juego."""

        while True:
            self._check_events()  # 05
            self._update_screen()  # 05
            self.clock.tick(60)  # 05

    def _update_screen(self):  # 02
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)  # 04
        self.ship.blitme()  # 04
        # Make the most recently drawn screen visible.
        pygame.display.flip()  # 04

    def _check_events(self):  # 01
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():  # 03
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
