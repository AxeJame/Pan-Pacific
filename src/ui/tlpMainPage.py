# Python imports

# Extron Library imports

# Project imports

# Define UI Objects
from devices import devTLPList

# Define UI Objects
from library.NavBasic import TLP_class
# Define UI Object Events

# TLP : start page reference

IDRoommodeDict = {
    'RoomModeSelect': 3000,
    'Room_1'        : 3001,           # ID ballroom 1
    'Room_1_name'   : 'Ballroom 01',
    'Room_2'        : 3002,           # ID ballroom 1
    'Room_2_name'   : 'Ballroom 02',
    'Combine_12'    : 1006,          # ID ballroom combine
    'Combine_12_name'   : 'Room Combine',
    'IDRoomText'    : 7015
}
IDControlDict = {
    'ViSwitch'              : 8301,           # ID Video switching
    'ViSwitch_name'         : 'VideoSwitch',
    'Audio'                 : 8302,           # ID Audio page
    'Audio_name'            : 'Audio',
    'Camera'                : 8303,          # ID Camera
    'Cam_name'              : 'Camera',
}

IDPopupPageDict = {
    'BR1_Audio'           : 'BR1 Audio control',
    'BR2_Audio'           : 'BR2 Audio control',
    'BRCombine_Audio'     : 'BRAll Audio control',
    'BR1_vswitch'         : 'BR1 video switch',
    'BR2_vswitch'         : 'BR2 video switch',
    'BRCombine_vswitch'   : 'BRAll video switch',
    'BR1_CamControl'      : 'Camera control BR1',
    'BR2_CamControl'      : 'Camera control BR2'
}

# (ID : id TLP, TLP, Room mode dictionary,Contro mode dictionary, Popup page dictionary)
for i in range(2):
    TLP_class.Roommode(i, devTLPList[i],IDRoommodeDict,IDControlDict,IDPopupPageDict)
    TLP_class.Controlmode(i, devTLPList[i],IDRoommodeDict,IDControlDict,IDPopupPageDict)

