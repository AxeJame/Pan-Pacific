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
from devices import devTLP

# Define UI Objects

# Define UI Object Events


# Labels customizing the TLP for this room
# Number button
btnPassNo1 = Button(devTLP, 1111)
btnPassNo2 = Button(devTLP, 1112)
btnPassNo3 = Button(devTLP, 1113)
btnPassNo4 = Button(devTLP, 1114)
btnPassNo5 = Button(devTLP, 1115)
btnPassNo6 = Button(devTLP, 1116)
btnPassNo7 = Button(devTLP, 1117)
btnPassNo8 = Button(devTLP, 1118)
btnPassNo9 = Button(devTLP, 1119)
btnPassNo0 = Button(devTLP, 1110)
btnPassDel = Button(devTLP, 1120)
btnPassGroup = MESet([btnPassNo1, btnPassNo2, btnPassNo3, btnPassNo4, btnPassNo5,
                      btnPassNo6, btnPassNo7, btnPassNo8, btnPassNo9, btnPassNo0, btnPassDel])
btnPassGroupDict = {
    btnPassNo1 : "1",
    btnPassNo2 : "2",
    btnPassNo3 : "3",
    btnPassNo4 : "4",
    btnPassNo5 : "5",
    btnPassNo6 : "6",
    btnPassNo7 : "7",
    btnPassNo8 : "8",
    btnPassNo9 : "9",
    btnPassNo0 : "0",
}
# Feedback Pass light
btnPassLight1 = Button(devTLP, 1121)
btnPassLight2 = Button(devTLP, 1122)
btnPassLight3 = Button(devTLP, 1123)
btnPassLight4 = Button(devTLP, 1124)
btnPassLightGroup = [btnPassLight1, btnPassLight2, btnPassLight3, btnPassLight4]
# pass feedback lable
lblLoginSystem = Label(devTLP, 1130)

# back button
btnPassBack = Button(devTLP, 1131)

# Navigation : back to start page
@eventEx(btnPassBack, 'Pressed')
def btnPassBackressed(button: Button, state: str):
    print(button.Name, state)
    lblLoginSystem.SetText('Login to system')
    devTLP.HideAllPopups()
    devTLP.ShowPage('Start')


# Pass login to system

keyPassMaster = "0000"
keyRef =""
keyCount = 0
def turnLight(count : int):
    for i in range(3):
        if i < count:
            btnPassLightGroup[i].SetState(1)
        else:
            btnPassLightGroup[i].SetState(0)


@eventEx(btnPassGroup.Objects, 'Pressed')
def btnPassGroupPressed(button: Button, state: str):
    global keyCount
    print(button.Name, state)
    if (button == btnPassDel) & (keyCount > 0):
        keyRef = keyRef[:-1]
        keyCount -= 1
        print(keyRef)
        turnLight(keyCount)
    elif (button != btnPassDel) & (keyCount < 4):
        keyRef = keyRef + btnPassGroupDict.get(button)
        keyCount += 1
        print(keyRef)
        turnLight(keyCount)
    if keyCount == 4:
        if keyRef == keyPassMaster:
            devTLP.ShowPage('Room mode')
        else:
            lblLoginSystem.SetText('Password is incorrect, Please again!')
        
        keyCount = 0
        keyRef = ""
        turnLight(keyCount)




    