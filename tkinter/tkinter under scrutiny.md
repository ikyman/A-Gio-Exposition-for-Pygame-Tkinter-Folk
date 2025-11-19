If you're reading this, you're doubtless aware of the sample code, guiInTkinter.py
Do you need to read it? Not particularly. Not only am I assumning the reader already has a baseline working knowledge on writing tkinter code, 
I will also do my very best to stuff enough MS Paint drawings into this explainer to expediate all explinations for this explainer.

# No user interation
Take the "Hello World" program: It runs. It exits. 
It ignores you and I. Once the user runs it, they can but watch.
This isn't ideal. I am a user, and I demand to be pampered!
# Text-based user interaction
Many programs give the user a command line and tell tham to get on with it. For many years, up to and including now, this was to program than a GUI. 
An example of a program with text-based interation:
`
[do you wish to add a (b)utton or (m)ove the shape? > m
[which direction should the shape move? > s
[your shape has moved 5 units south, and is now positioned at (10, 15) 
==Program Exited==
`

You might spot one minor pecadillo with this program: what if I want to move the shape twice?
I can't due to the structure of the program:
<img width="313" height="400" alt="image" src="https://github.com/user-attachments/assets/8683d16e-1c09-4825-8939-56a2f3c2c8ce" />

This can be fixed by running the inner "move shape or add button" section as long as the user wants. I.E. by using a while loop.
The program now looks like this:
<img width="490" height="326" alt="image" src="https://github.com/user-attachments/assets/4a771d8a-eec3-4741-bb67-be1364a9a1a8" />
Alternatively and oversimplified: 
<img width="748" height="487" alt="image" src="https://github.com/user-attachments/assets/ec91b1c3-691f-45d7-a494-9e79cc41607e" />


Now the entire program is a loop: it only exits when I input "e"
`
[do you wish to add a (b)utton, (m)ove the shape, or (e)xit? > e 
==Program Exited==
`
Great! I can move the shape or add buttons to my heart's content, exactly the behavior we want from our experimental GUI program.

 On second thoughts, it's not great. "Out of sight, out of mind". I do not see this shape. I don't see any buttons. Fake!

# mainloop()
I'm going to start off at the way, way bottom. We've already instantiated the tkinter Application Root with tk = Tk(). 
The real action, however, starts with tk.mainloop()! 
Recall the earlier commentary on the basic structure of a text-based program. The loop. With only tk.mainloop(), we reconstruct that loopy pattern!

<img width="750" height="487" alt="image" src="https://github.com/user-attachments/assets/33c9a6be-157a-4bf4-a632-dbd7901b7cc5" />

One caviat: if you're comparing this loop above with the loop from the text-based application, there's one small thing missing: By itself, mainloop() doesn't translate user input into actions. 
I would love to explain how input begats action. But before I do so, I would like even more to ramble and philosophize over the nature of the dummy program.

# One program? No, two!
Clicking a button has no effect on any shape, and moving a shape has no effect on any button.
This program is not one, but two. 
First, we have a movable shape on a canvas.
Secondly, we have the buttons which make more buttons. 

Each of these can be discuissed seperately, which I will do shortly. 
One moment! I will brag about my excellent S(olid) skills. I seperated the shape-moving and button-clicking into seperate modules. If I ever need to change either of them in the future, I can rest easy knowing that changes made in one class won't obliterate the other class. Extremely smart, that's what I am.

# I move the shape!
A shape that moves via arrow-keys. 

First of all, we got to make the canvas the shape is on, and the shape itself. These tasks are done before the mainloop, and so shall not affect our nice little cycle.
We shall do so by instantiating a Canvas object, packing it, and drawing the shape. The first two tasks are done in the if name == "main" conditional, the latter is done via the shape's constructor.

__Canvas__ : The name gives the game away, I say. Much like a real-life canvas, a tkinter canvas is needed if you ever need to draw anything. Polygons and circles are too chaotic to handle either packing or gridding.
To instantiate a widget like a canvas, it need the container it is "in". This determines the widget's future location in relation to other widgets through pack()ing or grid()ing. Being a Canvas, you'ld likely also want to describe the height, width, and background colour of the canvas. These can be set using the arguments `height, width, and background`

__Packing__ :  "Built-in the box" widgets like buttons (which we'll get to later) and the canvas need to be packed before use. This tells tkinter where each widget is placed in relation to existing and future widgets.
You can fine-tune where exactly a newly-packed widget is placed via both the side and anchor properties. I, being a professional jiggled these settings around untill my widgets were in the right position.
I recon that's not a particularly satisfying answer, and the Tkinter people agree! Hence, they created the grid() function. Like pack(), grid() places widgets on the screen. grid, being grid-based and objective, is easier to use than the Relatist pack(). More reading on grid() vs pack() can be found here: https://tkdocs.com/tutorial/concepts.html#geometry

__Shape Drawing__ : Much like how a canvas is needed to draw items, it would be useless to have a canvas and be unable to draw anything on it. Canvases can draw many items, such as polygons, rectangles, text, and images. Each of these drawn objects can be refered to by it's ID. 
In our case, we will be saving the polygon's id. When our shape is supposed to move, we can use canvas.move in conjunction with the polygon's ID to make the polygon move. Each direction has their own function.

But now is later. When and how will we move the shape? Your eyes may be drawn to the bind_all emporium. This is a cruicial step: it binds a select user action event to a particular function.
In other words, it bridges the user input with the doing the doings:

https://github.com/user-attachments/assets/1b322bfa-a5cb-4a52-b565-1e327a38d9d7

A picture is worth a thousand words, and the above video has 25 fps. I think enough has been said about bind_all.

# I press the button!
Buttons are widgets, much like canvas objects. As such, your new-found (or old-found) knowledge on pack()ing (or grid()-ing) should suffice to create and place a Button.
The text written on the button and the function run when the button is pressed can be set via arguments `text` and `command`, respectively.

# A Hydra Metaphor that gets increasengly strained over time.
The first button, when clicked, creates another button, as does the second button, as does the third, and so on. All of these buttons are the same!
When you really think about it, t'is just one button, with many heads:

<img width="364" height="280" alt="image" src="https://github.com/user-attachments/assets/b06a6047-bf5a-4746-8799-8fb3b1bcff5b" />

calling `Button` create a new button-creating button. It's a new head on the hydra. Great! Creating new heads is all we really need, given the specifications of the app.

Just one small problem: where shall these heads by allocated? 1 5-headed Hydra is easier to keep track of than 5 1-headed snakes. 

Hence, the ButtonManager class: It's the button-Hydra's body, so I don't go mad juggling around 5 1-headed body-less snakes.

<img width="726" height="508" alt="image" src="https://github.com/user-attachments/assets/1bd4723a-f27b-431d-9c1a-009fca6c94c3" />


# Frames and containerization
Ideally, our buttons should be one on top of the other, and have no need to 

The ButtonManager owns 2 things: the "Create a button" function, and the Frame in which newly created buttons are made. It's the button Zone.

# Ouch! Quit Poking me!
Let me tell you a tale from my youth. (This is utterly irrelavent to the implementation of the application)


