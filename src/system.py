"""
The system is the place to define system logic, automation, services, etc. as a whole.  It should
provide an *Initialize* method that will be called in main to start the start the system after
variables, devices, and UIs have been defined.

Examples of items in the system file:
* Clocks and scheduled things
* Connection of devices that need connecting
* Set up of services (e.g. ethernet servers, CLIs, etc.)
"""

# Python imports

# Extron Library imports
from devices import devTLPList
# Project imports

def Initialize():
    # Connect all devices
    # Show Start page
    devTLPList[0].ShowPage('Start')
    devTLPList[1].ShowPage('Start')
    devTLPList[2].ShowPage('Start')
    print('Show Start page')
    # Finish Initialize() with a print()
    print('System Initialized')
