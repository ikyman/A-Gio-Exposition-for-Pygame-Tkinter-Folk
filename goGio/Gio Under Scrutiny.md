# 2 Widgets, 3 Options

When I was initially learning the GIO UI Framework, I learned of a button. Much like how a Button is a Widget in Tkinter, a Button is a Widget.

We know a button is a widget because it uses the "Clickable" type, found in GIO's "widget" sub-package. 

A button is furthermore a material, a sub-package of the widget package. Surely, the Button's Widget credentials are unassailable. 

A Button is therefore quintessential Widget, Or so I assumed.
It would be therefore very confusing if there was a different type of widget! 

Now to displaying out button. We need to figure out where to place this button, where in the layout of my program the button will be situated.

There is a Go GIO Sub-Package for such layout issues: layout.

layout.Flex is what I used to seperate the canvas from the buttons. 
layout.Flex is named such from it's impressive ability to dynamically change the size of the displayed elements as the window size changes. 
It looks very elegant & "Modern" & "2020"s. 

layout.Flex displays FlexChildren. A FlexChild is a simple class containing the weighting (AKA How big this widget is compared to other elements) and the widget to be displayed.

Widgets! Yes, I am familiar with widgets from the Button. My next step is to search the widget sub-package for a canvas Widget, much like how I found the clickable button from the widget sub-package.

