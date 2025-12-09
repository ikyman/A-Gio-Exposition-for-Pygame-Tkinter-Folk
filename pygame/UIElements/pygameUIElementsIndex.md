# Surfaces

pygame.Surface: Object Representing something visible, be it your drawn doodles, text or a loaded image. https://www.pygame.org/docs/ref/surface.html

Surface.blit: "Bro Locare IRL Thusplace". blit()-ing a surface on top of another surface is required for anything drawn on surface 1 to be visible. https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

Surface.get_rect

Surface.fill: The shapes drawn on the Surface can get their own colours, why can't the surface itself be get a nice colour? Has to be called before drawing said shapes, lest this background colouring over-rules the shapes in the foreground. https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill

# Font

pygame.font

pygame.font.init

pygame.font.SysFont

Font

Font.Render

# Other

pygame.draw.rect

pygame.Rect

Rect.collidepoint

pygame.Color

pygame.MOUSEBUTTONDOWN

pygame.MOUSEMOTION

UIInteractable
