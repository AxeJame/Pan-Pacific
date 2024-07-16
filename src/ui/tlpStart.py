"""
This is the place to put the modules for each UI in the system.  One module for each unique ui --
mirrored panels should be in the same file.
* UI object definition
* UI navigation
"""

# Python imports

# Extron Library imports

# Project imports
from devices import devTLPList

# Define UI Objects
from library.NavBasic import TLP_class
# Define UI Object Events

# TLP : start page reference
IDStartPageDict = {
    'IDStaTile'     : 7001,           # ID Start tile
    'IDPrToBegin'   : 8000,           # Press To Begin button
    'IDStaText'     : 10000          # Start text label
}
TLP_class.PressToBegin(devTLPList[0],IDStartPageDict, name = 'Master')
TLP_class.PressToBegin(devTLPList[1],IDStartPageDict, name = 'Ipad Ballroom A')
TLP_class.PressToBegin(devTLPList[2],IDStartPageDict, name = 'Ipad Ballroom B')

        