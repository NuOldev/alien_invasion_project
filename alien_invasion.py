"""
Creando la clase padre del juego.
Creacion de la ventana donde aparecerán todos los elementos del juego.
Creando el loop principal del juego.
Manejo de control de eventos.
Control del frame rate del juego.
Estableciendo la apariencia del fondo de la ventana de juego.
"""

import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Overal class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()  # controlling frame rate
        self.settings = Settings()
        # Create a pygame window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # Surface
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""

        while True:  # Event loop
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)  # Frame rate at 60 times per second


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
