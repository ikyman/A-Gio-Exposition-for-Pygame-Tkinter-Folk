# I Lied #Oopsy #BadBoy
Quoth I: "Luckily, I used the programmer's favorite trick: The trusty ol' Copy-Paste! Voila! No AI 'Vibe Coding' Required!" 
I neglected to mention that I copy-pasted from an AI "vibe coded" project. Teehee!

# Front End Button.
This is the only true UI element that's being used: a SubCorrectingSurface's purpose is not be be seen, but to match the absolute coordinates with a particular surface's coordinates.
The Front End Button Does what it says on the tin: it runs the callback function every time the user clicks in the area covered by the button.

The front-end button is quite simple. Class initiation and drawing the button are both handled by the parent class, UIInteractable.

# UIInteractable
Th project I took the Front End Button from had buttons. Buttons are nice, but FREEDOM is nicer!
The UI interactible abstract super-class is a class that handles drawing the particular UI interactable.
Thus, whenever I want to add a new type of UI element, I simply make it a child of UI interactable.
Thus, I don't have to write seperate code for neither instantiating nor drawing this UI Element.

Class inheritence, baby!

# SubCorrectingSurface
I was tinkering with tkinter for quite a bit more time than I was down to game with Pygame.
In tkinter, you can organize UI elements with frames and pack()/grid(). 
I took this frame of mind to Pygame. I supposed the closest anology to frames were surfaces.
Thus, instead of putting a button in a frame, I put it on a surface.

This lead to a tiny, tiny problem: If you put a button on a surface, the button know it's own coordinates relative to the surface.
<img width="697" height="714" alt="image" src="https://github.com/user-attachments/assets/55bfd562-f195-44cb-82f0-5b0fea880643" />


The button object is snugly living in it's own little world, the surface.
Events are less cloistered. The Mouse position coordinates of an event refer to the display. I.E. the whole application, reguardless of which surface the mouse is hovering over. Ergo, 0,0 is around where the polygon is.

What happens if we don't make a correction? When the user hovers over the polgon at (10,10), an event is created. This event informs any consumer that the mouse is over (10,10). The button consumes this event, compares it to it's coordinates in relation to the parent surface, and gives the go-ahead. Thus, instead of clicking on the button, as is intuative, the user has to click in some vague area to the far left of the application. Unideal!

<img width="910" height="708" alt="image" src="https://github.com/user-attachments/assets/38ef2f44-0093-4320-8a16-92b0fb6bb570" />

What SubCorrectingSurface does is this: Each button now know the surface it's on. Before handiling any mouse-related events, it calls the SubCorrectingSurface to correct the event datapoints. 
With this fix, a button is no longer bamboozled by it's cozy living on a Surface.

Hopefully, this explainer is satisfactory. To a certain extent, I am satisfied: with this fix, I rarely have to think about the global coordinates vs surface coordinates dichotemy. But on the other hand, I can't help but feel there are more elegant solutions to this problem: if any experienced pygamers can explain how they approached this problem, it would be most welcome.

# UIDefaults
The UIinteractable, and by extension, the Front-End-Button, ask for quite a lot of parameters. 
The UIDefaults are, and this might come as a surprise, the Defaults for a lot of the cosmetic options for the Front-End-Button.
As the UIinteractable can pull in the defaults, I don't have the onerous burden of filling out all of a button's cosmetic options.
