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

<img width="750" height="476" alt="image" src="https://github.com/user-attachments/assets/b0873443-dc45-449c-8413-b481b2ebc369" />

