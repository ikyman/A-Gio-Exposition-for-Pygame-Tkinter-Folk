from tkinter import *

DEFAULT_CANVAS_WIDTH = 500
DEFAULT_CANVAS_HEIGHT = 500
DEFAULT_CANVAS_BACKGROUND_COLOR = 'cyan'

class MovableShape():
 def __init__(self, canvas, fillColour, borderColour, borderWeight, shapePoints, speed = 5):
  self.canvas = canvas
  self.shape = self.canvas.create_polygon(shapePoints, fill = fillColour, outline=borderColour, width = borderWeight)
  self.speed = speed
  canvas.bind_all("<KeyPress-Up>", self.moveUp)  
  canvas.bind_all("<KeyPress-Right>", self.moveRight)
  canvas.bind_all("<KeyPress-Down>", self.moveDown)
  canvas.bind_all("<KeyPress-Left>", self.moveLeft)  

 def moveUp(self, event):
  self.canvas.move(self.shape, 0, -self.speed) 
  
 def moveRight(self, event):
  self.canvas.move(self.shape, self.speed, 0) 
  
 def moveDown(self, event):
  self.canvas.move(self.shape, 0, self.speed)  

 def moveLeft(self, event):
  self.canvas.move(self.shape, -self.speed, 0)


class ButtonManager():
 def __init__(self, container):
  self.container = container
  self.buttonCount = 0
  self.addButton()
 def addButton(self):
  self.buttonCount += 1;
  newButton = Button(self.container, text = "Button Number {}".format(self.buttonCount), command = self.addButton)
  newButton.pack(side = 'top')

if __name__ == "__main__":
 tk=Tk()
 tk.title("Polygon & Button Application")
 polygonCanvas=Canvas(tk,
                      height=DEFAULT_CANVAS_WIDTH,
                      width=DEFAULT_CANVAS_HEIGHT,
                      background=DEFAULT_CANVAS_BACKGROUND_COLOR)
 buttonList = Frame(tk)
 
 polygonCanvas.pack(side = "left")
 buttonList.pack(anchor = NE, side = "right")
 
 buttonManager = ButtonManager(buttonList)
 movableShape = MovableShape(polygonCanvas, 'black', 'red', 4, [(32, 0), (0, 25), (13, 64), (64, 51), (64, 25)])

 tk.mainloop() 