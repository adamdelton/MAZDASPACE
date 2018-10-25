from appJar import gui

# create the GUI with title
app = gui("MX5")

# add contents
app.addButton("LED Test", press)

# start GUI
app.go()
