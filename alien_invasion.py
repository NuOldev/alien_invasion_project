"""
Responding to a keypress and release keypress
Allowing Continous Movement
Moving both Left and Right
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
            self._check_events()  # helper method, internal call
            self.ship.update()  # external call, Ship class method
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Keypress event
            elif event.type == pygame.KEYDOWN:  # si se presiona una tecla...
                if event.key == pygame.K_RIGHT:  # si es a la derecha...
                    self.ship.moving_right = True  # ...
            elif event.type == pygame.KEYUP:  # si se suelta la tecla
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False  # ...


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
