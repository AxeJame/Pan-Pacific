"""
This is the place to put the modules for each UI in the system.  One module for each unique ui --
mirrored panels should be in the same file.
* UI object definition
* UI navigation
"""

# Python imports

# Extron Library imports

# Project imports

# Define UI Objects

import ui.tlpStart
import ui.tlpPassword

# import tlpMatrixSwitcher
# import tlpPassword

# Define UI Object Events


# Khai báo màn hình







# b1 = tlpLabel(devTLP).labelA
# b1.SetText('in B1')

# a1 = tlpLabel(devTLP).buttonA
# @eventEx(a1, 'Pressed')
# def a1Pressed(button: Button, state: str):
#     print(button.Name, state)
#     if button.State == 0:
#         b1.SetText('BallroomA')
#         button.SetState(1)
#     elif button.State == 1: 
#         b1.SetText('BallrA')
#         button.SetState(0)


# b = tlpLabel(devIpad1).labelA
# b.SetText('in B1')
# a = tlpLabel(devIpad1).buttonA
# @eventEx(a, 'Pressed')
# def a2Pressed(button: Button, state):
#     print(button.Name, state)
#     if button.State == 0:
#         b.SetText('BallroomB')
#         button.SetState(1)
#     else: 
#         b.SetText('BallrB')
#         button.SetState(0)


# b = Label(devIpad1, 7001)
# b1 = Button(devIpad1, 8000)
# @eventEx(b1, 'Pressed')
# def b1Pressed(button, state):
#     print(button.Name, state)
#     b.SetText('Ballroom Ipad')
