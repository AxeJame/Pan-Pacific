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
from extronlib import event
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
        self.labelA = Label(UIhost, 7001) 
        self.buttonA = Button(UIhost, 8000)

L = Label(devTLP, 10000)
L.SetText('test 01')


b1 = tlpLabel(devTLP).labelA
b1.SetText('in B1')

a1 = tlpLabel(devTLP).buttonA
@eventEx(a1, 'Pressed')
def a1Pressed(button: Button, state: str):
    print(button.Name, state)
    if button.State == 0:
        b1.SetText('BallroomA')
        button.SetState(1)
    elif button.State == 1: 
        b1.SetText('BallrA')
        button.SetState(0)


b = tlpLabel(devIpad1).labelA
b.SetText('in B1')
a = tlpLabel(devIpad1).buttonA
@eventEx(a, 'Pressed')
def a2Pressed(button: Button, state):
    print(button.Name, state)
    if button.State == 0:
        b.SetText('BallroomB')
        button.SetState(1)
    else: 
        b.SetText('BallrB')
        button.SetState(0)


# b = Label(devIpad1, 7001)
# b1 = Button(devIpad1, 8000)
# @eventEx(b1, 'Pressed')
# def b1Pressed(button, state):
#     print(button.Name, state)
#     b.SetText('Ballroom Ipad')
