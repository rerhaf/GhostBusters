import sys
import pygame
import time
from settings import Settings
from ship import Ship
pygame.mixer.init()
pygame.mixer.music.load("Ghostbusters.mp3") 
pygame.mixer.music.play(-1,0.0)
class GhostBusters:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ghost Busters")
        
        self.ship = Ship(self)
        # Set the background color.
        #self.bg_color = (230, 230, 230)
        #path = C:\Users\Jan\Desktop\Ghost busters
        #playsound('Ghostbusters.mp3')
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # Watch for keyboard and mouse events.
            #playsound('Ghostbusters.mp3')
    def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            # Move the ship to the right.
            #self.ship.rect.y += 1
            # Redraw the screen during each pass through the loop.
    def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = GhostBusters()
    ai.run_game()
