from tkinter import *

DEFAULT_CANVAS_WIDTH = 500
DEFAULT_CANVAS_HEIGHT = 500
DEFAULT_CANVAS_BACKGROUND_COLOR = 'cyan'

class MovableShape():
 def __init__(self, canvas, fillColour, borderColour, borderWeight, shapePoints, speed = 5):
  self.canvas = canvas
  self.shape = self.canvas.create_polygon(shapePoints, fill = fillColour, outline=borderColour, width = borderWeight)
  self.speed = speed
  self.canvas.bind_all("<KeyPress-Up>", self.moveUp)  
  self.canvas.bind_all("<KeyPress-Right>", self.moveRight)
  self.canvas.bind_all("<KeyPress-Down>", self.moveDown)
  self.canvas.bind_all("<KeyPress-Left>", self.moveLeft)  

 def moveUp(self, event):
  self.canvas.move(self.shape, 0, -self.speed) 
  print("moved", self.canvas.coords(self.shape))
  
 def moveRight(self, event):
  self.canvas.move(self.shape, self.speed, 0) 
  
 def moveDown(self, event):
  self.canvas.move(self.shape, 0, self.speed)  

 def moveLeft(self, event):
  self.canvas.move(self.shape, -self.speed, 0)


class ButtonManager():
 def __init__(self, container, packRow, packColumn, packAnchor):
  self.buttonFrame = Frame(container)
  self.buttonFrame.grid(row = packRow, column = packColumn, sticky = packAnchor)
    
  self.buttonCount = 0
  self.addButton()
  
 def addButton(self):
  self.buttonCount += 1;
  newButton = Button(self.buttonFrame, text = "Button Number {}".format(self.buttonCount), command = self.addButton)
  newButton.grid(row = self.buttonCount -1, column = 1)

if __name__ == "__main__":
 tk=Tk()
 tk.title("Polygon & Button Application")
 polygonCanvas=Canvas(tk,
                      height=DEFAULT_CANVAS_WIDTH,
                      width=DEFAULT_CANVAS_HEIGHT,
                      background=DEFAULT_CANVAS_BACKGROUND_COLOR
                      )
 
 polygonCanvas.grid(row = 0, column = 0)

 movableShape = MovableShape(polygonCanvas, 'black', 'red', 4, [(32, 0), (0, 25), (13, 64), (64, 51), (64, 25)]) 
 buttonManager = ButtonManager(tk, 0, 1, NW)

 tk.mainloop() 