# Widgets
In Tkinter, Possible UI elements take the shape of Objects, called Widgets. Widgets handle user input events and draw themselves as needed. All this is done self-contained: No additional code is required within the Mainloop.
https://tkdocs.com/tutorial/widgets.html

The following two methods are common to all Widgets:

pack(): "Locate and display this current widget in relation to the other widgets stored in this container". A closer analogue to Go GIO's Layout than grid()

&

grid(): Like Pack, but by coordinates. Removes the need to remember what Widget was where when wondering where one other widget would be
https://tkdocs.com/tutorial/concepts.html#geometry

Button: A Button. Click it, and something interesting might happen! As long there's a function set as the button's command, that is. https://tkdocs.com/pyref/button.html

<KeyPress-Up>: Sample Event. In this Particular case, <KeyPress-Up> is the event identifier for pressing the up arrow key. This shares the documentation page with other Event identifiers at https://tkdocs.com/shipman/event-types.html
The list of named keys can be found here: https://tkdocs.com/shipman/key-names.html

Canvas: The Widget responsable for displaying doodles and non-interactable text. https://tkdocs.com/pyref/canvas.html

Canvas.bind_all: Instructs Tkinter to run a particular handler every time a specified event is triggered. bind_all will run the specified function irrespective of what tkinter widget is currently "in focus" https://tkdocs.com/shipman/binding-levels.html 

Canvas.create_polygon: Draw a polygon with specified points. Returns an identifier which can later be used for subsequent adjustments. Documentation for Canvas.create_polygon specificaly is on the Canvas documentation page at https://tkdocs.com/shipman/canvas.html . There is also a documentation page on the returned object identifier at https://tkdocs.com/shipman/canvas-oid.html , though the documentation page doesn't add much above my already-short summary of create_polygon.

Canvas.move: One of the "Subsequent adjustments" Moves the item denoted by an identifier by a set number of pixels. Shares the documentation page with other "subsequent adjustments" at https://tkdocs.com/shipman/canvas-methods.html

Frame

# Non-Widgets

Tk() Initializes Tk and returns an empty container for packing widgets into. https://tkdocs.com/pyref/tk.html

tk.mainloop

tk.title

