# Aren't I tired of adding all the location information to whenever I want to add a button? 
# Hence the purpose of this class; It is one line. Whenever I add a UI Item, it goes down to the next item on the rail.

from .front_end_button import FrontEndButton

## WARNING: AI WRITTEN: MAY NOT WORK, YOU KNOW HOW AI IS

## Furthermore, This does not fly WRT code Quality. A whole bunch of this code does the same darn thing.
## Most of these items are inherited by ui_interactable. Why do we have seperate codes for "Post a button" &
## "Post a Textarea" if the whole point of this class is to say "Heck, I don't care, post it, put the thing into position,
## Irreguardless of what that thing is"

class PostingRail():
    def __init__(self, surfaceCoordCorrector, x, start_y=20, padding=10):
        """
        Initialize a posting rail for automatic UI element positioning.
        
        Args:
            surfaceCoordCorrector: The surface coordinate corrector object
            x: Fixed x coordinate for all elements on this rail
            start_y: Starting y coordinate for the first element
            padding: Vertical spacing between elements
        """
        self.surfaceCoordCorrector = surfaceCoordCorrector
        self.fixed_x = x
        self.current_y = start_y
        self.padding = padding
        self.last_element_height = 0
        self.elements = []  # Track all elements posted on this rail
    
    def add_button(self, width, height, text, callback=None, colour=None, hover_colour=None):
        """
        Add a button to the posting rail.
        
        Args:
            width: Width of the button
            height: Height of the button
            text: Button text
            callback: Function to call when button is clicked
            colour: Button color (optional)
            hover_colour: Button hover color (optional)
            
        Returns:
            FrontEndButton: The created button
        """
        # Calculate position
        x = self.fixed_x
        y = self.current_y
        
        # Create the button
        button = FrontEndButton(
            self.surfaceCoordCorrector, x, y, width, height, text, callback, 
            colour=colour, hover_colour=hover_colour
        )
        
        # Add to rail's element list
        self.elements.append(button)
        
        # Update position for next element
        self.current_y += height + self.padding
        self.last_element_height = height
        
        return button
    
    def draw_all(self):
        """Draw all elements posted on this rail."""
        for element in self.elements:
            element.draw()
    
    def handle_events(self, event):
        """Handle events for all elements posted on this rail."""
        for element in self.elements:
            element.handle_event(event)
    
    def get_next_position(self, element_height=30):
        """
        Get the next position for a UI element on this rail.
        Useful for custom elements that don't have a dedicated add method.
        
        Args:
            element_height: Height of the element being positioned
            
        Returns:
            tuple: (x, y) coordinates for the next element
        """
        # Calculate position
        x = self.current_x
        y = self.current_y
        
        # Update for next element
        self.current_y += self.last_element_height + self.padding
        self.last_element_height = element_height
        
        return (x, y)
 