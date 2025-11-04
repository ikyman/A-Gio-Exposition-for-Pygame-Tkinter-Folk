import pygame
import copy


from UIElements.front_end_button import FrontEndButton
from UIElements.sub_correcting_surface import SubCorrectingSurface

pygame.font.init()
FONT_SIZE = 20
UI_FONT = pygame.font.SysFont("Niagara Engraved" ,FONT_SIZE )
FONT_COLOUR = "black"

DEFAULT_CANVAS_WIDTH = 500
DEFAULT_CANVAS_HEIGHT = 500
DEFAULT_CANVAS_BACKGROUND_COLOR = 'cyan'
DEFAULT_SIDEBAR_WIDTH = 200


class MovableShape:
    def __init__(self, canvas, fillColour, borderColour, borderWeight, shapePoints, speed = 5):
        
        self.canvas = canvas
        self.speed = speed
        self.fillColour = fillColour
        self.borderColour = borderColour
        self.borderWeight = borderWeight
        
        self.coords = copy.copy(shapePoints)
    
    def draw(self):
        pygame.draw.polygon(self.canvas, self.fillColour, self.coords)
        pygame.draw.polygon(self.canvas, self.borderColour, self.coords, width = self.borderWeight)                
    
    def handle_key_input(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_UP]:
            self.move2d( (0, -self.speed) )
        if pressed_keys[pygame.K_RIGHT]:
            self.move2d( (self.speed, 0) )
        if pressed_keys[pygame.K_DOWN]:
            self.move2d( (0, self.speed) )
        if pressed_keys[pygame.K_LEFT]:
            self.move2d( (-self.speed, 0) )
    
    def move2d(self, vec2d):
        self.coords = list(map( lambda c: (c[0] + vec2d[0], c[1] + vec2d[1]), self.coords) )
        
     
class ButtonManager():
    BUTTON_WIDTH = DEFAULT_SIDEBAR_WIDTH
    BUTTON_HEIGHT = 40
    
    def __init__(self, container, coords_size , sideBarColor):
        self.buttonSidebar = SubCorrectingSurface(container, coords_size, sideBarColor)
        self.buttonList = []
        self.addButton()
        
    def addButton(self):
        y_position = ButtonManager.BUTTON_HEIGHT*len(self.buttonList)
        newButton = FrontEndButton(self.buttonSidebar, 0, y_position, ButtonManager.BUTTON_WIDTH, ButtonManager.BUTTON_HEIGHT,  text = "Button Number {}".format(len(self.buttonList)+1), callback = self.addButton)
        self.buttonList.append(newButton)
        
    def handle_event(self, event):
        for button in self.buttonList:
            button.handle_event(event)
    def draw(self):
        self.buttonSidebar.blit_to_main()
        for button in self.buttonList:
            button.draw()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Polygon & Button Application")
    running = True
    clock = pygame.time.Clock()
    
    
    all_display = pygame.display.set_mode((DEFAULT_CANVAS_WIDTH + DEFAULT_SIDEBAR_WIDTH, DEFAULT_CANVAS_HEIGHT))
    polygonCanvas = pygame.Surface( (DEFAULT_CANVAS_WIDTH, DEFAULT_CANVAS_HEIGHT) )
    buttonSideBar = ButtonManager(all_display, (DEFAULT_CANVAS_WIDTH, 0, DEFAULT_SIDEBAR_WIDTH, DEFAULT_CANVAS_HEIGHT), "mediumorchid3")
    moveableShape = MovableShape(polygonCanvas, "gainsboro", "deeppink4", 5, [(32, 0), (0, 25), (13, 64), (64, 51), (64, 25)] )
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            buttonSideBar.handle_event(event)
        
        moveableShape.handle_key_input()
        
        all_display.blit(polygonCanvas, (0,0) )       
        polygonCanvas.fill("seagreen1")  
        moveableShape.draw()     
        buttonSideBar.draw()  
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    quit()