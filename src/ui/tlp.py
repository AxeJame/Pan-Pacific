"""
This is the place to put the modules for each UI in the system.  One module for each unique ui --
mirrored panels should be in the same file.
* UI object definition
* UI navigation
"""

# Python imports

# Extron Library imports
from extronlib.system import MESet
from extronlib.ui import Button, Label

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTLP, devIpad1

# Define UI Objects

# import tlpStart
# import tlpMatrixSwitcher
# import tlpPassword

# Define UI Object Events

class tlpLabel:
    def __init__(self, TLP):
        self.TLP = TLP
        UIhost = self.TLP
        self.label_a = Label(UIhost, 7001) 
        self.button_a = Button(UIhost, 8000)

a = tlpLabel(devTLP).label_a
a.SetText('Ball')
a1 = tlpLabel(devTLP).button_a
@eventEx(a1, 'Pressed')
def a1Pressed(button: Button, state):
    print(button.Name, state)
    if state == 'Pressed':
        a.SetText('BallroomA')
        button.SetState(1)
    else: 
        a.SetText('BallrA')
        button.SetState(0)
 


b = Label(devIpad1, 7001)
b1 = Button(devIpad1, 8000)
@eventEx(b1, 'Pressed')
def b1Pressed(button, state):
    print(button.Name, state)
    b.SetText('Ballroom Ipad')