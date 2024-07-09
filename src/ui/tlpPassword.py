"""
This is the place to put the modules for each UI in the system.  One module for each unique ui --
mirrored panels should be in the same file.
* UI object definition
* UI navigation
"""

# Python imports

# Extron Library imports

# Project imports
from devices import devTLP, devIpadList, devIpad1, devIpad2

# Define UI Objects
from library.NavBasic import TLP_class
# Define UI Object Events


# Labels customizing the TLP for this room
# Number button

IDPwDict = {                #ID password dict
    'btnPassNo1' : 1111,
    'btnPassNo2' : 1112,
    'btnPassNo3' : 1113,
    'btnPassNo4' : 1114,
    'btnPassNo5' : 1115,
    'btnPassNo6' : 1116,
    'btnPassNo7' : 1117,
    'btnPassNo8' : 1118,
    'btnPassNo9' : 1119,
    'btnPassNo0' : 1110,
    'btnPassDel' : 1120,
    'btnPassPageClose' : 1131,
    'keyPassMaster'    : "0000",
    'nextPagePw'       : 'Room mode',                  # the next page after login
    'btnPassLight1' : 1121,
    'btnPassLight2' : 1122,
    'btnPassLight3' : 1123,
    'btnPassLight4' : 1124,
    'lblLoginSystem' : 1130,
    'btnPassBackToStart' : 1131 

}

IDPwDict2 = {                #ID password dict
    'btnPassNo1' : 1111,
    'btnPassNo2' : 1112,
    'btnPassNo3' : 1113,
    'btnPassNo4' : 1114,
    'btnPassNo5' : 1115,
    'btnPassNo6' : 1116,
    'btnPassNo7' : 1117,
    'btnPassNo8' : 1118,
    'btnPassNo9' : 1119,
    'btnPassNo0' : 1110,
    'btnPassDel' : 1120,
    'btnPassPageClose' : 1131,
    'keyPassMaster'    : "1234",
    'nextPagePw'       : 'Room mode',                  # the next page after login
    'btnPassLight1' : 1121,
    'btnPassLight2' : 1122,
    'btnPassLight3' : 1123,
    'btnPassLight4' : 1124,
    'lblLoginSystem' : 1130,
    'btnPassBackToStart' : 1131 

}

TLP_class.LoginAVSystem(devTLP, IDPwDict)
TLP_class.LoginAVSystem(devIpad1, IDPwDict2)
TLP_class.LoginAVSystem(devIpad2, IDPwDict)

