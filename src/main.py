"""
The main program entrance file.  The contents of this should be:
* Identification of the platform and version.
* imports of the project components
* Call to initialize the system
"""

# Python imports

# Extron Library Imports
from extronlib import Platform, Version

print('ControlScript', Platform(), Version())

# Project imports
import variables
print('Done import variables')
import devices
print('Done import devices')
import ui.tlp
print('Done import TLP')
import control.av
print('Done import Control.av')
import system

system.Initialize()
