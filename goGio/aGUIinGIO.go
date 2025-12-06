package main

/*import pygame
import copy


from UIElements.front_end_button import FrontEndButton
from UIElements.sub_correcting_surface import SubCorrectingSurface

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
*/
import(
    "fmt"

    _"image"
    "image/color"
    "os"

	"gioui.org/app"
    "gioui.org/f32"
    "gioui.org/op/clip"
    "gioui.org/op"
    "gioui.org/op/paint"
    "gioui.org/layout"
    "gioui.org/widget"
    "gioui.org/widget/material"
    /*
    "log"
	"time"*/

)

func drawPolygon(operationManager *op.Ops, points []f32.Point) *clip.Path{
    polygon := new(clip.Path)
    polygon.Begin(operationManager);
    for _, point := range points {
        polygon.MoveTo(point)
    }
    polygon.Close()
    return polygon
}

type buttonManager struct{
    //buttonFrame
    buttonCount int
    buttonClickTracker widget.Clickable
    buttonTheme *material.Theme 

}

func newButtonManager() buttonManager{
    bm := new(buttonManager);
    bm.buttonCount = 0
    bm.buttonTheme = material.NewTheme() 
    return *bm
}

func (bm *buttonManager) addButton(){
    bm.buttonCount = bm.buttonCount + 1;

    /*new_button_name := fmt.Sprintf("Button Number %d.", bm.buttonCount);
    new_button := material.Button(buttonTheme, &buttonTemplate, new_button_name);
    */
}

func (bm *buttonManager) drawButtons(gtx layout.Context) layout.Dimensions{
    var buttonFrame layout.Flex
    buttonFrame.Axis = layout.Vertical

    buttonFlexChilds := make([]layout.FlexChild,0)
    th := material.NewTheme()
    buttonSize := gtx
    buttonSize.Constraints.Max.Y=20;

    for i:=0; i<bm.buttonCount; i++ {
        buttonFlexChilds = append(buttonFlexChilds, layout.Flexed (1, material.Button(th, &bm.buttonClickTracker, fmt.Sprintf("Button Nubmer %d" , i )).Layout ) )
    }    
   
    return buttonFrame.Layout (gtx, buttonFlexChilds...)
}

func drawCanvas(gtx layout.Context) layout.Dimensions{
    canvasDims := new(layout.Spacer)
    canvasDims.Width = 500
    return canvasDims.Layout(gtx)
}

func main(){
    
	go func(){
        w := new(app.Window)
		ops := new(op.Ops)
        w.Option(app.Title("Polygon & Button Application"))

        bm := newButtonManager()
        bm.addButton();

		for {
            evt := w.Event()

			switch typ := evt.(type){
			case app.FrameEvent:
                flexContext := app.NewContext( ops, typ)

                //split_screen_context.Constraints= layout.Exact(image.Point{X: 40,Y: 40})

                var axisLeftRight layout.Flex;

                axisLeftRight.Layout(flexContext, layout.Flexed(  4, drawCanvas ), layout.Flexed(1, bm.drawButtons)  )


                paint.Fill(ops, color.NRGBA{R: 252, G:0, B: 255})
                //drawPolygon(ops, []f32.Point{f32.Point{X: 0, Y: 0}, f32.Point{X: 100, Y: 0}, f32.Point{X: 100, Y: 100}, f32.Point{X: 0, Y: 100}})


                typ.Frame(ops);

                
			case app.DestroyEvent:
				os.Exit(0)
			}
		}
	}()
	app.Main()

}