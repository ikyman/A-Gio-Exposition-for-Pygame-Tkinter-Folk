import pygame
from .ui_interactable import UIInteractable

class FrontEndButton(UIInteractable):
    def __init__(self, surfaceCoordCorrector, x, y, width, height, text, callback=None, 
    colour = None, hover_colour = None):
        super().__init__(surfaceCoordCorrector, x, y, width, height, text, colour_unfocused = colour, colour_focused = hover_colour)
        self.callback = callback
        
    def draw(self):
        """Draw the button on the given surface"""
        super().draw()        
    
    def handle_event(self, event):
        """Handle pygame events for this button"""
        if event.type == pygame.MOUSEMOTION:
            self.is_focused = self.is_point_inside(event.pos)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_point_inside(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False
