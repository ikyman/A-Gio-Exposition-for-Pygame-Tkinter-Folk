import pygame

pygame.font.init()

class UIDefaults:
    """Global UI settings and constants"""
    # Button colors
    UI_ELEM_NORMAL = (200, 200, 200)
    UI_ELEM_SPECIAL = (180, 180, 180)
        
    # Borders
    BORDER_WIDTH = 2
    BORDER_COLOR =  "black"
    
    # Fonts
    FONT_SIZE = 20
    UI_FONT = pygame.font.SysFont("Niagara Engraved" ,FONT_SIZE )
    FONT_COLOUR = "black"