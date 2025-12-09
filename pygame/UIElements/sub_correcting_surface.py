import pygame

class SubCorrectingSurface:
    """
    Takes a surface and manages all the correction math so UI elements don't have to worry about it.
    """
    
    def __init__(self, parent_surface, coords, colour = "tan"):
        """parent_surface: What this surface will be blitted onto
           coords: (x,y,width,height)"""
        self.parent_surface = parent_surface
        self.x = coords[0]
        self.y = coords[1]
        self.width = coords[2]
        self.height = coords[3]

        self.surf = pygame.Surface( (self.width, self.height))
        self.surf.fill(pygame.Color(colour ) )
    
    def get_corrected_pos(self, uncorrected_pos):
        """Convert global coordinates to surface-relative coordinates"""
        return (uncorrected_pos[0] - self.x, uncorrected_pos[1] - self.y)
    
    def blit_to_main(self):
        """Blit this surface to the main display at the specified position"""
        self.parent_surface.blit(self.surf, (self.x, self.y))
    