class Settings:
   """A class to store all settings for Alien Invasion."""
   def __init__(self):
       """Initialize the game's settings."""
       # Screen settings
       self.screen_width = 500
       self.screen_height = 400
       self.bg_color = (100, 200, 200)
       # Ship settings
       self.ship_speed = 1.5