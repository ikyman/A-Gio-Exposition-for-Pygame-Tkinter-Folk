# Pygame

pygame.display: used for controlling the the display window. https://www.pygame.org/docs/ref/display.html

pygame.display.flip

pygame.display.set_caption: Sets the window's caption. Equivelent to Tkinter's tk.title. https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption

pygame.display.set_mode: Initilize the Pygame applications' window, as well as setting the size of said window. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

pygame.draw: Module for drawing shapes on a surface. https://www.pygame.org/docs/ref/draw.html

pygame.draw.polygon: Draws on a Surface a polygon of a given colour and with a given set of points. https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon

pygame.init()

pygame.quit

pygame.Surface: Object Representing something visable, be it your drawn doodles, text or a loaded image. https://www.pygame.org/docs/ref/surface.html

Surface.blit: "Bro Locare IRL Thusplace". blit()-ing a surface ontop of another surface is required for anything drawn on surface 1 to be visible. https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

Surface.fill

# Pygame Events

pygame.event: Module for interacting with events. https://www.pygame.org/docs/ref/event.html

pygame.event.get(): Get a list of all the events that happened since the last calling of pygame.event.get(). https://www.pygame.org/docs/ref/event.html#pygame.event.get

pygame.key: Module for keyboard interaction. https://www.pygame.org/docs/ref/key.html

pygame.key.get_pressed()

pygame.event.Event

Event.type

# Event Types

pygame.QUIT: Integer associated with x-ing out of Pygame. Not to be confused with pygame.quit(). pygame.QUIT, like all Event.type s is an Enum-ed integers under the hood. As such, it has dedicated detailed documentation. You can find a list of other Event type s at https://www.pygame.org/docs/ref/event.html

The following are all constants representing the keyboard keys for a specific direction. They do not have their own dedicated page, but a list of keyboard constants can be found at https://www.pygame.org/docs/ref/key.html

pygame.K_UP

pygame.K_RIGHT

pygame.K_DOWN

pygame.K_LEFT

# Pygame Clock

pygame.time: Module for pygame's time-related functions. https://www.pygame.org/docs/ref/time.html

pygame.time.Clock: Object for monitering time. https://www.pygame.org/docs/ref/time.html#pygame.time.Clock

Clock.tick: Calculates the number of milliseconds between frames. Required every tick. Without callign Clock.tick, psooooooom! Mach 8 billion! Doublely-Lightning Warp Drive! Which sounds fun, untill the computer player zips across the map at light speed and kills you less than a second after the game begins. https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick

# Other

copy.copy

FrontEndButton: My class. Triggers a callback if a click event intersects with it. https://github.com/ikyman/A-Gio-Exposition-for-Pygame-Tkinter-Folk/blob/main/pygame/UIElements/UI%20element%20Review.md

SubCorrectingSurface: A rectangle drawn on a surface does not necessarily share the same Coordinate system as mouse events. A SubCorrectingSurface provides an interfacet for coordinate correction for any UI elements drawn on the SubCorrectingSurface. https://github.com/ikyman/A-Gio-Exposition-for-Pygame-Tkinter-Folk/blob/main/pygame/UIElements/UI%20element%20Review.md
