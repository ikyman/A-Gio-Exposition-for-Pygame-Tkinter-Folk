import pygame
from .ui_defaults import UIDefaults

# The List of parameters is too long, especially for child components
#https://refactoring.guru/design-patterns/builder

class UIInteractable:
    """
    Base class for all UI elements that can be interacted with.
    Handles common functionality like coordinate correction, drawing, and event handling.
    """
    def __init__(self, surfaceCoordCorrector, 
    x, y, width, height, 
    text,
    colour_unfocused = None,
    colour_focused = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

        self.surfaceCoordCorrector = surfaceCoordCorrector

        
        self.colour_unfocused = UIDefaults.UI_ELEM_NORMAL if not colour_unfocused else colour_unfocused
        self.colour_focused = UIDefaults.UI_ELEM_SPECIAL if not colour_focused else colour_focused
        
        self.is_focused = False
        self.font = UIDefaults.UI_FONT
    
    def get_corrected_pos(self, uncorrected_pos):
        """Apply position correction offset"""
        if self.surfaceCoordCorrector:
            return self.surfaceCoordCorrector.get_corrected_pos(uncorrected_pos)
        return uncorrected_pos
    
    def is_point_inside(self, pos):
        """Check if a point is inside this UI element"""
        corrected_pos = self.get_corrected_pos(pos)
        return self.rect.collidepoint(corrected_pos)
    
    def draw(self):
        colour = self.colour_focused if self.is_focused else self.colour_unfocused

        # Draw background
        pygame.draw.rect(self.surfaceCoordCorrector.surf, pygame.Color(colour), self.rect)
        
        # Draw border
        pygame.draw.rect(self.surfaceCoordCorrector.surf, pygame.Color(UIDefaults.BORDER_COLOR), self.rect, UIDefaults.BORDER_WIDTH)

        text_surface = self.font.render(self.text, True, pygame.Color(UIDefaults.FONT_COLOUR) )
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surfaceCoordCorrector.surf.blit(text_surface, text_rect)


