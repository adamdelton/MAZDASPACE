#!/usr/bin/env python3

from appJar import gui

# button functions
def press(btn):
    print(btn)

# create the GUI with title
app = gui("MX5")

# add contents
app.addButton("LED Test", press)

# start GUI
app.go()
