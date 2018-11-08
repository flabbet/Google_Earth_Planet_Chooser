import subprocess
from appJar import gui

def open_planet(file):
    subprocess.call("start " + file, shell=True)

def press(button):
    open_planet("Planets/{0}.KML".format(button))

app = gui("Google Earth Planet Chooser", "200x100", showIcon=False)
app.setBg("#F19D38", override=True, tint=True)
app.setFg("black", override=True)
app.addLabel("title", "Choose Planet")
app.setLabelFg("title", "#212121")
app.addButtons(["Earth", "Mars", "Moon"], press)
app.setButtonBg("Earth" ,"#4F4CAA")
app.setButtonFg("Earth", "#A6C070")
app.setButtonBg("Mars" ,"#B34D24")
app.setButtonFg("Mars" ,"white")
app.setButtonBg("Moon" ,"#C9C9C9")
app.setButtonFg("Moon" ,"Black")
app.go()


