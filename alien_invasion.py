"""
01 - Importando modulos externos (sys, pygame)
02 - Importando modulos internos (Creados para el programa; ship, settings)
03 - Creando la clase padre del juego.
04 - Creacion de la ventana para los elementos del juego (surface).
05 - Creando el loop principal del juego.
06 - Manejo de control de eventos.
07 - Control del frame rate del juego.
08 - Dibujando la apariencia de la ventana en cada paso por el loop principal.
09 - Creando instancia para uso del modulo settings.
10 - Creando instancia para uso del modulo ship.
11 - Dibujando la nave en la posicion correcta en cada paso por el loop.
12 - Creando instancia de clase principal para correr el juego.
"""

# 01
import sys
import pygame
# 02
from settings import Settings
from ship import Ship


class AlienInvasion:  # 03
    """Clase general para manejar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Iniciar el juego y crear sus recursos."""
        pygame.init()

        self.clock = pygame.time.Clock()  # 07
        self.settings = Settings()  # 09
        # Create a pygame window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # 04
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # 10

    def run_game(self):
        """Iniciar el loop principal del juego."""

        while True:  # 05
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():  # 06
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)  # 08
            self.ship.blitme()  # 11

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)  # 07 - Frame rate at 60 times per second


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()  # 12
    ai.run_game()
