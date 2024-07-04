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
from devices import devTLP, devIpadList, devIpad1

# Define UI Objects

# Define UI Object Events

# TLP : start page
class TLP_start:
    List = []
    def __init__(self, PanelAlias):
        self.TLP = PanelAlias
        UIhost = self.TLP
        TLP_start.List.append(self)

        '''=== Start '''
        self.lblStartTitleText = Label(UIhost, 7001)


        self.lblStartRoomText = Label(UIhost, 10000)

        '''=== Begin '''

        self.btnStart = Button(UIhost, 8000)
        

        # btnClosePassPage = Button(UIhost, 1131)
        # @eventEx(btnClosePassPage, 'Pressed')
        # def btnStartEvent(button: Button, state: str):
        #      print(button.Name, state)  
        #      devTLP.HidePopup('Password Popup')
''' =============================================================================================================================='''






for tlp in devIpadList:   
    TLP_start(tlp).lblStartTitleText.SetText('BALLROOM')
    TLP_start(tlp).lblStartRoomText.SetText('Audio Visual System')

    @eventEx(TLP_start(tlp).btnStart, 'Pressed')
    def btnStartPressed(button: Button, state: str):
        print(button.Name, state)
        tlp.ShowPage('Password page')
        