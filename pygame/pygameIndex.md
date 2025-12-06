# Pygame

pygame.display: used for controlling the display window. https://www.pygame.org/docs/ref/display.html

pygame.display.flip: Put down the pen, I am done drawing. Flipping off all the visuals for a frame in one flipping function has two benefits: the user is at no risk of seeing an incomplete frame (Or worse, a complete frame flashing with an incomplete frame). It also saves the GPU the trouble of drawing something, only to draw over it less than a second later. https://www.pygame.org/docs/ref/display.html#pygame.display.flip

pygame.display.set_caption: Sets the window's caption. Equivelent to Tkinter's tk.title. https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption

pygame.display.set_mode: Initilize the Pygame applications' window, as well as setting the size of said window. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

pygame.draw: Module for drawing shapes on a surface. https://www.pygame.org/docs/ref/draw.html

pygame.draw.polygon: Draws on a Surface a polygon of a given colour and with a given set of points. https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon

pygame.init(): Intialize Pygame. This is something you should do in more complicated projects, though for the example application in this tutorial, commenting out python.init() did nothing. https://www.pygame.org/docs/ref/pygame.html#pygame.init

pygame.quit(): Unintitialize Pygame. https://www.pygame.org/docs/ref/pygame.html#pygame.quit

pygame.Surface: Object Representing something visible, be it your drawn doodles, text or a loaded image. https://www.pygame.org/docs/ref/surface.html

Surface.blit: "Bro Locare IRL Thusplace". blit()-ing a surface on top of another surface is required for anything drawn on surface 1 to be visible. https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

Surface.fill: The shapes drawn on the Surface can get their own colours, why can't the surface itself be get a nice colour? Has to be called before drawing said shapes, lest this background colouring over-rules the shapes in the foreground. https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill

# Pygame Events

pygame.event: Module for interacting with events. https://www.pygame.org/docs/ref/event.html

pygame.event.get(): Get a list of all the events that happened since the last calling of pygame.event.get(). https://www.pygame.org/docs/ref/event.html#pygame.event.get

pygame.key: Module for keyboard interaction. https://www.pygame.org/docs/ref/key.html

pygame.key.get_pressed(): What keys do I currently have presssssssssssseeeeeeeeeeedddddddd dddddddddddoooooooowwwwwwwwwwwnnnnnnnnnnn????????????? https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

pygame.event.Event: Pygame Object Representing an Something Happening, such as a mouse click. https://www.pygame.org/docs/ref/event.html#pygame.event.Event

Event.type: Something happened. Was it a Mouse click? This Object-Field doesn't have it's own dedicated page, but documentation for the event object is found at https://www.pygame.org/docs/ref/event.html#pygame.event.Event , and the list of Event type s are here: https://www.pygame.org/docs/ref/event.html

# Event Types

pygame.QUIT: Integer associated with x-ing out of Pygame. Not to be confused with pygame.quit(). pygame.QUIT, like all Event.type s is an Enum-ed integers under the hood. As such, it has dedicated detailed documentation. You can find a list of other Event type s at https://www.pygame.org/docs/ref/event.html

The following are all constants representing the keyboard keys for a specific direction. They do not have their own dedicated page, but a list of keyboard constants can be found at https://www.pygame.org/docs/ref/key.html

pygame.K_UP

pygame.K_RIGHT

pygame.K_DOWN

pygame.K_LEFT

# Pygame Clock

pygame.time: Module for pygame's time-related functions. https://www.pygame.org/docs/ref/time.html

pygame.time.Clock: Object for monitoring time. https://www.pygame.org/docs/ref/time.html#pygame.time.Clock

Clock.tick: Calculates the number of milliseconds between frames. Required every tick. Without calling Clock.tick, psooooooom! Mach 8 billion! Doublely-Lightning Warp Drive! Which sounds fun, until the computer player zips across the map at light speed and kills you less than a second after the game begins. https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick

# Other

copy.copy: "I want the values of this list/container/object. I don't want the list/container/object to be at risk of modifications by any other users of this list/container/object, so much so that I'm willing to take the computing power to make a my own, private version of the list/container/object" https://docs.python.org/3/library/copy.html#module-copy

copy.deepcopy: Not in guiInPygame.py, but it's hard to talk about deepcopy. If the list/container/object has list/container/objects inside of it, copy.copy doesn't copy the list-ception. deepcopy does. https://docs.python.org/3/library/copy.html#module-copy

FrontEndButton: My class. Triggers a callback if a click event intersects with it. https://github.com/ikyman/A-Gio-Exposition-for-Pygame-Tkinter-Folk/blob/main/pygame/UIElements/UI%20element%20Review.md

SubCorrectingSurface: A rectangle drawn on a surface does not necessarily share the same Coordinate system as mouse events. A SubCorrectingSurface provides an interface for coordinate correction for any UI elements drawn on the SubCorrectingSurface. https://github.com/ikyman/A-Gio-Exposition-for-Pygame-Tkinter-Folk/blob/main/pygame/UIElements/UI%20element%20Review.md
