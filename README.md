# A-Gio-Exposition-for-Pygame-Tkinter-Folk
An Tutorial/Overview of Python's GUI Libraries, and a Compare &amp; Contrast with Go's GIO.

# Why this Tutorial?
GIO already has a tutorial: https://jonegil.github.io/gui-with-gio/ 

I found this tutorial after being inflicted by a goodly urge to make a GUI with Go. Gio had the coolest name of the Googled Go GUI libraries, so I went with that.

I have already made GUIs in Tkinter and Pygame, two Python libraries. I have also used React.

I subjectively judged "Writing code in GoLang" to be more akin to Python. GoLang has a Blue Gopher, and one of the Python Logo's snakes is Blue. Boom! Science! Same language!

Tkinter, at least for me, came out of the box when installing Python. Pygame is a bit more esoteric. I had to Pip-install it. 

Tkinter is advertized on the box as a GUI library. Pygame is advertized as a game library. Video Games display Graphics and allow the User to Interact with them. They're a kind of GUI. They don't embody GUI Purity, though. The raw GUI essence is watered down by phrases such as "Wolf killed another sheep" and "Unguarded Heavy Cruiser? Meet your new buddies: 6 Salvage Corvettes"

Gio is advertized as a GUI Library. Much like Tkinter. Therefore, these two libraries must be the same. Logic! 

Thus, I skimmed through the GIO tutorial searching for tkinter keywords like "Canvas" or "Button" or "bind_all".

This did not work. Tkinter and GIO are quite different.

I already have Knowledge on Python GUI-Making. Why should there not be a tutorial which can channel such already-existing POWER?

# The GUI Application
Our program, the one which will be discussed and trilingually translated, is as thus:
You are greeted with a screen, with a shape and a button:

<img width="410" height="332" alt="image" src="https://github.com/user-attachments/assets/60ba38cf-9496-4c94-b4b5-95b416bf8297" />

Using WASD Moves the shape. Simple enough.

Your eyes may focus upon the button: If you click that, what do you get? A second button. 
But wait? Now that this secret second button is revealed, what does that button do? It creates a third button. 
In fact, if you click the second button a second time, you get a fourth button.

This isn't some grand button puzzle: Any button, including future buttons, adds a new button. Simple enough.

Indeed, the whole point of this app is to be "Simple Enough". This one Dummy program draws shapes, reacts to keyboard input, reacts to mouse input, and dynamically adds elements.

Learning how to code a GUI that draws shapes, reacts to keyboard input, reacts to mouse input, and dynamically add elements is jolly good.
Any future GUIs you may program is bound to have at least one of these elements, and for that this tutorial has you covered!

# Disclaimer
This is a public GitHub Repository, meaning you, the reader, are free to provide feedback. 
Of especially valued feedback are the following:
If, by some odd sequence of events, you, despite being on GitHub, are a non-coder, your feedback is prized above all. I decree that this Tutorial should be Suis Generus (E.G. Je ne sans pas) be a jolly good read. Something one would conceivably read even without the urges of GUI-making bearing down upon them. Thus, I would very much any non-programmers feedback on the per-se entertainment value of this informative tutorial

More mundane matters, the structure of this tutorial is focused on a core on Tkinter. The unique perspective is explaining how the other GUI Libraries relate to Tkinter. Tkinter is the library I've Tinkered with most of all. I have less experience with pygame, and this very tutorial shall be my first GIO App.

Judgement on either field would also be Top-Notch.

Lastly, if public is clamoring for it, I will add a React Section to this tutorial.

# Tutorial Structure
This tutorial is split up into three sections: Tkinter, Pygame, and Go/Gio.

Each implementation has their own folder. Each folder contains: The Code for the implementation, the commentary on said code, and an index.

We start off with Tkinter, I'm writing this tutorial with an understanding that Tkinter is the GUI library people are most familiar with.
Still, I recommend reading this section: This is the one explaining the skeleton of a GUI application, a conceptualization which we will be returning back to multiple times during this tutorial. 

The Idea behind this tutorial is to take a Tkinter GUI, strip it down to it's theoretical skeleton, and re-build it with different types of meat. Doing so requires watching a tkinter-body get dissolved in knowledge-acid.

We then hop over to pygame, to view a different method of writing a GUI in python. Not only is the language the same, but the skeleton of the GUI application is similar.

Finally, we head on over to GIO, the library that this tutorial is attempting to explain. We're now in unfamiliar territory, but with the power of friendship (AKA the other GUIs), GIO will be unable to srop your newfound POWERS! It shall be crushed into dust! 

Each folder also contains the code for an implementation. I am trying my best to render reading these unnecessary: The idea is to explain things so fantastically that any reader would be enlightened to such an extent that his or her command of the learning material is absolute, solely from the tutorial explanations.


Writing such a tutorial is easier said than done. Hence the code to follow-along in case I fail. Further preparations for my inexorable miserable flubbing of this assignment can be seen in the Index pages: These allow a reader to hyper-link jump to the documentation for any items in the libraries under discussion, In case my discussion is insufficient.
