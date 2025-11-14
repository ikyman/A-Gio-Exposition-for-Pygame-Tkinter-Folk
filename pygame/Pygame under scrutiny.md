# UIElements Folder

First of all, you may be wondering why there's a "UIElements" folder. 
The answer is quite simple: Pygame doesn't have any built-in UI elements. On one hand, this may be annoying.
On the other hand, I took a quite refresher of my collection of video games and found that no two had exactly the same UI.

This lack fo UI elements could be worse: Imagene, for example, the most popular developer platform, a company with billions of dollars of revinue, millions of users, and thousands of employes failed to integrate Spellcheck.
Imagine again, that that very same company got purchased by microsoft, yet fials to be able to read Word documents.

Now that, that would be an embaressment! Far more of a ball-dropping than a Game library not implementing UI elements on the assumption that no two games would have the same UI!

Luckily, I used the programmer's favorite trick: The trusty ol' Copy-Paste! Voila! No AI "Vibe Coding" Required!

I will not give a comprehensive review of what my UI elements are, for multiple reasons.
1. This is really a Gio GUI tutorial, with only a stop-by on tkinter and Pygame
2. They should work, shouldn't they? 
3. I aim for this tutorial to emphisize the codebase as little as possible. I started off with Tkinter for program conceptualization.
   From said conceptualization, from the structure of the program, I aim to show the simularities of all three programs.
   Think think with the mindset, see how the concepts fit together.

# It's still the same old loop
<img width="748" height="487" alt="image" src="https://github.com/user-attachments/assets/dce0abb2-6f88-441c-be9a-bc3e99336bb4" />

You might recognize this loop from "Tkinter under scruitiny". Indeed, one point I want to stress during this entire tutorial is how, irrespective of which library one choses, the blueprint of the GUI stays mostly the same. 
I say "Mostly", because here's the ms paint drawing de jour for pygame:

<img width="967" height="598" alt="image" src="https://github.com/user-attachments/assets/63ecdd7c-6e7d-42cc-b205-7035f6ddaaba" />

Wow! What a Kaleidoscope! 

# While mainloop is more concise, while main loop is more explicit
I used a while loop for the pygame program's mainloop.

Why is this ordered in such a way? Now that the whileloop is explicit and not tucked away in the one mainloop() function, I can see in which order the "get user input and take action" and "draw the objects" are in, and I have "getting user input and take action" first.

# Pygame: It's different: drawing is required 
With Tkinter, I drew my shape before entering the loop. Upon moving my shape with move(), it moved. 
Does it rerender? I don't know. Tkinter handled it, it worked, I didn't question it. 

With pygame, each object has to be drawn ever tick. My buttons and my Polygon objects both call their respective pygame.draw() functions every tick.

Now, do you remember how, with tkinter you had to pack() or grid() your Canvas, frame and Button widgets? The rest of the program could be ay-ok. You haven't pack()-ed though. The program doesn't know where to display the widget. With such freedom of choice, it takes the easiest path: doing diddly squat.

Blit-ting and surfaces act in a similear manner. The buttons may be drawn upon a Surface, yes. The surface is floating in the ether, though. Where specifically is this surface? Who knows? Thus, nothing on the surface gets displayed.
surfaceGruff.blit(surfaceFairy, (10,10) ) is surfaceGruff telling surfaceFairy to quit it's namby-pamby imaginaryland prancing and get it's ass down to earth at coordinates (10, 10).
Thus, you should view "blit" as an acronym, "Bro Locate Irl Thusplace". (That's not the real etymology. The real etymology is An homage to an esoteric and unpopular wikipedia page: https://en.wikipedia.org/wiki/Bit_blit)

Nowhere does "Bro Locate Irl Thusplace" imply that the surface gets coloured.
If you, say, forget to fill the canvas after moving a shape, you get the Solitaire victory effect:

<img width="700" height="529" alt="image" src="https://github.com/user-attachments/assets/56e4424e-4231-4cdc-b69c-ed09439b4a9e" />

It's a cool effect after winning solitaire. While playing solitaire, though, It'll cause pandemonium.

# Event handling by passing off

Event handling is furthermore much more explicit. Instead of calling bind to pass in a function, we simply feed the event to each interactable object.



For more Pygame Tutorials to scratch you Pygame Itch, I found Sentdex useful: https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
