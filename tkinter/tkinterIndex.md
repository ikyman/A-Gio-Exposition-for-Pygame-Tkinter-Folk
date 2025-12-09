# Widgets
In Tkinter, Possible UI elements take the shape of Objects, called Widgets. Widgets handle user input events and draw themselves as needed. All this is done self-contained: No additional code is required within the Mainloop.
https://tkdocs.com/tutorial/widgets.html

The following two methods are common to all Widgets:

pack(): "Locate and display this current widget in relation to the other widgets stored in this container". A closer analogue to Go GIO's Layout than grid()

&

grid(): Like Pack, but by coordinates. Removes the need to remember what Widget was where when wondering where one other widget would be
https://tkdocs.com/tutorial/concepts.html#geometry

Button

<KeyPress-Up>

Canvas: The Widget responsable for displaying doodles and non-interactable text. https://tkdocs.com/pyref/canvas.html

Canvas.bind_all

Canvas.coords

Canvas.create_polygon

Canvas.move

Frame

# Non-Widgets

Tk() Initializes Tk and returns an empty container for packing widgets into. https://tkdocs.com/pyref/tk.html

tk.mainloop

tk.title

