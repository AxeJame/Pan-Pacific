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
from devices import devTLP, devIpadList, devIpad1, devIpad2

from extronlib.device import ProcessorDevice, UIDevice
# Define UI Objects
from library.NavBasic import TLP_class
# Define UI Object Events

# TLP : start page reference
IDStartPageDict = {
    'IDStaTile'     : 7001,           # ID Start tile
    'IDPrToBegin'   : 8000,           # Press To Begin button
    'IDStaText'     : 10000,          # Start text label
}
TLP_class.PressToBegin(devTLP,IDStartPageDict)
TLP_class.PressToBegin(devIpad1,IDStartPageDict)
TLP_class.PressToBegin(devIpad2,IDStartPageDict)




# for tlp in devIpadList:   
#     TLP_start(tlp).lblStartTitleText.SetText('BALLROOM')
#     TLP_start(tlp).lblStartRoomText.SetText('Audio Visual System')

#     @eventEx(TLP_start(tlp).btnStart, 'Pressed')
#     def btnStartPressed(button: Button, state: str):
#         print(button.Name, state)
#         tlp.ShowPage('Password page')
        