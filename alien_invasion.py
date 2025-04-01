"""
Creando la ventana donde aparecerán todos los elementos del juego.
"""

import sys
import pygame


class AlienInvasion:
    """Overal class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))  # Surface
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""

        while True:  # Event loop
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
